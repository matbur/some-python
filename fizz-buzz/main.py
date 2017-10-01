from collections import OrderedDict
from functools import reduce
from itertools import compress
from operator import mul


def get_one(num: int, rules: dict, selectors: list):
    for selector in selectors:
        compressed = list(compress(rules, selector))
        multiplied = reduce(mul, compressed, 1)
        if multiplied == 1:
            continue
        if num % multiplied == 0:
            return ''.join([rules[i] for i in compressed])
    return num


def foo(rules: dict):
    rules = OrderedDict(sorted(rules.items()))

    n = len(rules)
    selectors = [[int(j) for j in f'{i:0>{n}b}'] for i in range(1 << n)]
    selectors = sorted(selectors, key=lambda x: x.count(1), reverse=True)

    for i in range(1, 111):
        print(get_one(i, rules, selectors))


def main():
    rules = {
        3: 'Fizz',
        5: 'Buzz',
        7: 'Mezz',
        11: 'Rozz',
    }
    foo(rules)


if __name__ == '__main__':
    main()
