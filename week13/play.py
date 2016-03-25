# class Iterable:
#     def __init__(self, iterable_one, iterable_two):
#         iterable_three = concat(iterable_one, iterable_two)

#     def __iter__(self, ):
#         pass

#     def __next__(self):
#         pass

# def chain(iterable_one, iterable_two):
#     iterable_three = Iterable(iterable_one, iterable_two)
#     return iterable_three


# print(list(chain(range(0, 4), range(4, 8))))

import itertools
from itertools import compress as itco
iter1 = range(0, 4)
iter2 = range(4, 8)

def chain(iter1, iter2):
    iter3 = itertools.chain(iter1, iter2)
    return iter3

print(list(chain(iter1, iter2)))


def compress(iterable, mask):
    s = itertools.compress(iterable, mask)
    return  s

print(list(itco(["Ivo", "Rado", "Panda"], [False, True, True])))


def cycle(x):
    return itertools.cycle(x)
# endless = cycle(range(0,10))
# for item in endless:
#     print(item)

# import time
# def cycle(x):
#     # for c in cycle:
#     #     x.append(c)
#     # return itertools.cycle(x)
#     # while True:
#     #     yield x
#     #     for i in x:
#     #     time.sleep(1)

# endless = cycle(range(0,10))
# for item in endless:
#     print(item)


def reader():
    f = open('001.txt', 'r')
    i = 0
    line = f.readline()
    buf = ''
    # counter = 0
    while not line.startswith('#'):
        buf += line
    print(buf)

    print(line)

reader()
