""" Module contains functions necessary to get all posts from django blog.
"""

import json
import re
from datetime import datetime
from multiprocessing.pool import Pool
from queue import Queue, Empty
from time import time

import requests
from bs4 import BeautifulSoup

URL = 'https://www.djangoproject.com/weblog/?page='
PAT = re.compile(r'<strong>(.*)</strong> on (.*) </span>')
H2PAT = re.compile(r'<h2>(.*)</h2>')


def get_links(url):
    """ Function gets links to all posts in blog.
    """
    try:
        page_request = requests.get(url)
    except requests.exceptions.ConnectionError as err:
        print(err)
        return get_links(url)
    page_bs = BeautifulSoup(page_request.content, 'html.parser')
    links = []
    for link in page_bs.find_all('a'):
        if link.get('class') == ['link-readmore']:
            links.append(link.get('href'))
    print(len(links), url)
    return links


def get_entry(link):
    """ Function gets all information about post given by link.
    """
    try:
        entry_request = requests.get(link)
    except requests.exceptions.ConnectionError as err:
        print(err)
        return get_entry(link)
    entry_bs = BeautifulSoup(entry_request.content, 'html.parser')
    for div in entry_bs.find_all('div'):
        if div.get('role') == 'main':
            contents = div.contents
            title = H2PAT.findall(str(contents[1]))[0]
            author, pub_date = PAT.findall(str(contents[3]))[0]
            it = iter(('first_name', 'last_name'))
            author = {i: j for i, j in zip(it, author.split())}
            pub_date = datetime.strptime(pub_date, '%B %d, %Y').strftime('%Y-%m-%d')
            content = ''.join(map(str, contents[5:-3]))
            print(pub_date)
            return {
                'title': title,
                'author': author,
                'pub_date': pub_date,
                'content': content,
            }


def queue2list(queue):
    """ Function changes queue into list.
    """
    out_list = []
    while not queue.empty():
        out_list.append(queue.get())
    return out_list


def drain(queue):
    """ Function yields values from queue until it is empty.
    """
    while True:
        try:
            yield queue.get_nowait()
        except Empty:
            break


def main():
    """ Function makes whole job.
    """
    queue = Queue()
    pages = (URL + str(i + 1) for i in range(44))

    t0 = time()

    with Pool(10) as p:
        for links in p.imap_unordered(get_links, pages):
            for link in links:
                queue.put(link)

    t1 = time()

    with Pool(20) as p:
        for entry in p.imap_unordered(get_entry, drain(queue)):
            queue.put(entry)

    t2 = time()

    print()
    print(t1 - t0)
    print('entries:', queue.qsize())
    print(t2 - t1)

    with open('data.json', 'w') as f:
        json.dump(queue2list(queue), f)


if __name__ == '__main__':
    main()
