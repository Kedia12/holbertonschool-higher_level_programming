#!/usr/bin/python3
"""
Module defining a FlyingFish class that extends the Fish class.
The FlyingFish class adds the ability to fly in addition to swimming.
"""


class Fish:
    """
    A simple Fish class with swimming capability.
    """
    def swim(self):
        """
        Simulate the fish swimming.
        args:
            None
        returns:
            str: A message indicating the fish is swimming.
        """
        print("The fish is swimming.")

    def habitat(self):
        """
        Return the habitat of the fish.
        args:
            None
        returns:
            str: A message indicating the fish's habitat.
        """
        print("The fish lives in water.")


class Bird:
    """
    A simple Bird class with flying capability.
    """
    def fly(self):
        """
        Simulate the bird flying.
        args:
            None
        returns:
            str: A message indicating the bird is flying.
        """
        print("The bird is flying.")

    def habitat(self):
        """
        Return the habitat of the bird.
        args:
            None
        returns:
            str: A message indicating the bird's habitat.
        """
        print("The bird lives in the sky.")


class FlyingFish(Fish, Bird):
    """
    A FlyingFish class that inherits from both Fish and Bird,
    combining swimming and flying capabilities.
    """
    def fly(self):
        """
        Simulate the flying fish soaring.
        args:
            None
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Simulate the flying fish swimming.
        args:
            None
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Return the habitat of the flying fish.
        args:
            None
        """
        print("The flying fish lives both in water and the sky!")
