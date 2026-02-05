#!/usr/bin/python3
"""Module that provides a counted iterator for tracking iteration progress."""


class CountedIterator:
    """An iterator wrapper that keeps track of the number of items iterated."""

    def __init__(self, iterator):
        """Initialize the CountedIterator with an iterable and reset counter.

        Args:
            iterator: An iterable object to be wrapped.
        """
        self.__iterator = iter(iterator)
        self.__counter = 0

    def get_count(self):
        """Return the number of items that have been iterated so far.

        Returns:
            int: The count of items fetched from the iterator.
        """
        return self.__counter

    def __next__(self):
        """Fetch the next item from the iterator and increment the counter.

        Returns:
            The next item from the wrapped iterator.

        Raises:
            StopIteration: When the iterator is exhausted.
        """
        try:
            self.__counter += 1
            return next(self.__iterator)
        except StopIteration:
            self.__counter -= 1
            raise StopIteration
