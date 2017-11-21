import collections  # Best
import platform

# from collections import namedtuple  # OK if used everywhere, but loses namespace info
# from collections import *  # BAD
import os

NamedTupleExample = collections.namedtuple('NamedTupleExample', 'height, length, width, density')

print(platform.system())  # to discover platform running code (Win/Linux/OSX)


def foo(text: str):  # helps intellisense
    return text


class ExampleBase():
    def __init__(self, length):
        self.length = length


class ExampleDerived(ExampleBase):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width


def factorial(n):  # recursion
    if n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(limit):  # Method
    nums = []
    current = 0
    next = 1
    while current < limit:
        current, next = next, next + current
        nums.append(current)
    return nums


def fibonacci_co(limit):  # Generator method/coroutine (consumes value and does something). Lots to learn here.
    current = 0
    next = 1
    # while current < limit:
    while True:
        current, next = next, next + current
        yield current


print('Via lists')
for n in fibonacci(100):
    print(n, end=', ')
print()
print('Via yield')
for n in fibonacci_co(100):
    if n > 10000:  # can't do this if it's a normal method?
        break
    print(n, end=', ')


# yield from is a thing:
def search_file(full_item, text):
    yield


def search_folders(folder, text):
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_folders(full_item, text)  # better yet, don't store matches, call sub-generator

        else:
            yield from search_file(full_item, text)


# Resume with project 9
