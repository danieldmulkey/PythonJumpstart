import collections  # Best
import platform

# from collections import namedtuple  # OK, but loses namespace info
# from collections import *  # BAD

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

# Resume with project 8