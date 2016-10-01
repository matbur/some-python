#!/usr/bin/python3.5

from series import Series


def main():
    words = {}
    letters = {}

    s = Series('friends')
    for ss in s.seasons:
        for e in ss.episodes:
            for l in e.lines:
                for w in l.words:
                    words[w] = words.get(w, 0) + 1
                    for ll in w.letters:
                        letters[ll] = letters.get(ll, 0) + 1

    sorted_letters = [(i, v) for (i, v) in sorted(letters.items(), key=lambda x: x[1], reverse=True)]
    for i in sorted_letters:
        print(i)
    print(len(sorted_letters))

    sorted_words = [(i, v) for (i, v) in sorted(words.items(), key=lambda x: x[1], reverse=True)]
    for i in sorted_words:
        print(i)
    print(len(sorted_words))


if __name__ == '__main__':
    main()
