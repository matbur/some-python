from flask import Flask, render_template, redirect
from jinja2.exceptions import TemplateNotFound

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


responses = {
    '238.html': 'No... the 38 is a little bit above the 2...',
    '274877906944.html': redirect('map.html'),
    'linkedlist.html': 'linkedlist.php'
}


@app.route('/<name>')
def template(name):
    return responses.get(name) or render_template(name)


@app.errorhandler(TemplateNotFound)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
