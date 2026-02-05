#!/usr/bin/python3
"""
Module defining a SwimMixin class that provides swimming and flying
capabilities.
"""


class SwimMixin:
    """
    Mixin class that provides swimming capability.
    """
    def swim(self):
        """
        Simulate swimming action.
        args:
            None
        returns:
            str: A message indicating swimming action.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that provides flying capability.
    """
    def fly(self):
        """
        Simulate flying action.
        args:
            None
        returns:
            str: A message indicating flying action.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits swimming and flying capabilities
    from SwimMixin and FlyMixin.
    """

    def roar(self):
        """
        Simulate the dragon roaring.
        args:
            None
        returns:
            str: A message indicating the dragon is roaring.
        """
        print("The dragon roars!")
