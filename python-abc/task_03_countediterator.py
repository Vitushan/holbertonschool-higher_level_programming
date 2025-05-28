#!/usr/bin/python3
"""
This is a module for interpreting python3
"""


class CountedIterator:
    """
    This is a countedIterator class
    """
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        return self.count
