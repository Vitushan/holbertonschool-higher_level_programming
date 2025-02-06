#!/usr/bin/python3
"""
this function extend the python list class
"""


class VerboseList(list):
    """
    This class should print a notification message
    every time an item is added
    """
    pass

    def append(self, item):
        """
        add an element to list and print message
        """
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """
        print message after extending the list
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {count} items.")

    def remove(self, value):
        """
        removing the item from the list and print a message
        """
        super().remove(value)
        print(f"Removed {value} from the list.")

    def pop(self, index=-1):
        """
        delete an element to the list   nd print a message
        """
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item
