#!/usr/bin/python3
"""
...
"""


class CountedIterator:
    """
    count iterator
    """

    def __init__(self, iterator):
        self.iterator = iter(iterator)
        self.count = 0
    
    def __next__(self):
        """
        ...
        """
        obj = next(self.iterator)
        self.count += 1
        return obj
        if obj > len(obj):
            raise StopIteration

    def get_count(self):
        """
        ...
        """
        return self.count
