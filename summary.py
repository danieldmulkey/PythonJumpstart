import os
import platform
import collections  # Best

# from collections import namedtuple  # OK if used everywhere, but loses namespace info
# from collections import *  # BAD

try:  # one way to work on Py2 and Py3 simultaneously
    import statistics
except:  # broad except clauses are bad, but this is A way to establish compatibility...
    # error code instead
    import statistics_standin_for_py2 as statistics

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
print()


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


# List comp:
x = [0, 1, 2, 3, 4, 5]
y = [t ** 2 for t in x if t > 1]  # list comp to access repeatedly
print('y by list comp is', y)
y = (t ** 2 for t in x if t > 1)  # gen expr to consume once
print('y by gen exp is', y.__next__())

# lambda arg: return is good for inline function

# @staticmethod  # deals with class/type, not instance of class/the object --> staticmethod --> no self

# Elaborate on dicts:

# DICTIONARIES FOR DISPARATE TYPES OF RELATED DATA:
lookup = {}
lookup = dict()
lookup = {'age': 42, 'loc': 'Italy'}
lookup = dict(age=42, loc='Italy')


class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level


gandalf = Wizard('Gandalf', 42)

print(gandalf.__dict__)  # NB! Dictionaries basis of objects in Python!

print(lookup)
print(lookup['loc'])  # says dict value lookup is extremely fast

if 'cat' in lookup:
    print(lookup['cat'])

lookup['cat'] = 'Fun code demos'

if 'cat' in lookup:
    print(lookup['cat'])

# DICTIONARIES FOR DIFFERENT INSTANCES OF HOMOGENEOUS DATA:
# Store a homogeneous set of data and find it by key. So use the dictionary as a
# temporary structure in order to more quickly find your answer.
# Original data type --> dict --> find by key. Want to find it by a different key? Make a
# new dictionary.
# NB: Can only use one field at a time (id, or name, or email) since dict takes key
# and value only, but it's extremely fast if you know which one you want to search with.
# Suppose these came from a data source (database, web service, etc.) and we want to
# randomly access them
import collections

User = collections.namedtuple('user', 'id, name, email')
users = [
    User(1, 'user1', 'user1@talkpython.fm'),
    User(2, 'user2', 'user2@talkpython.fm'),
    User(3, 'user3', 'user3@talkpython.fm'),
    User(4, 'user4', 'user4@talkpython.fm')
]

# build search dict from namedtuple content:
lookup = dict()
for u in users:
    lookup[u.id] = u

print(lookup[3])

for u in users:
    lookup[u.email] = u
print(lookup['user4@talkpython.fm'])


# Put try/except immediately in event loop --> increased stability, assuming you handle exceptions well
# (That was the main note from app 10, really)

# OH! dict.get('key') vs. dict['key']: get() returns None if 'key' isn't present, ['key'] returns an error.
