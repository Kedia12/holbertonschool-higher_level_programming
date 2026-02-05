#!/usr/bin/python3
"""
Module defining a VerboseList class that extends the built-in list.
This class overrides append, remove, pop, and extend methods to print
messages whenever these methods are called.
"""


class VerboseList(list):
    """
    A list that prints messages on modifications.
    Inherits from the built-in list and overrides append, remove, pop,
    and extend methods to provide verbose output.
    """
    def append(self, object):
        """
        Append an object to the list and print a message.
        args:
            object: The object to be appended to the list.
        returns:
            None
        """
        print(f"Added {object} to the list.")
        return super().append(object)

    def remove(self, object):
        """
        Remove an object from the list and print a message.
        args:
            object: The object to be removed from the list.
        returns:
            None
        """
        print(f"Removed {object} from the list.")
        return super().remove(object)

    def pop(self, index=-1):
        """
        Pop an object from the list and print a message.
        args:
            index: The index of the object to pop. Defaults to -1
            (the last item).
        returns:
            The popped object.
        """
        popped_value = super().pop(index)
        print(f"Popped {popped_value} from the list.")
        return popped_value

    def extend(self, iterable):
        """
        Extend the list with an iterable and print a message.
        args:
            iterable: An iterable to extend the list with.
        returns:
            None
        """
        print(f"Extended the list with {iterable}.")
        return super().extend(iterable)
