#!/usr/bin/env python3
"""
task_01_pickle.py

Pickling Custom Classes:
- Serialize and deserialize CustomObject instances using pickle.
- On missing/malformed files, return None as required.
"""

import pickle


class CustomObject:
    """A simple custom object that can be pickled to/from a file."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in the required format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize (pickle) the current instance into `filename`.
        Return self on success, None on failure.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)
            return self
        except (OSError, pickle.PickleError, AttributeError, TypeError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize (unpickle) an instance from `filename`.
        Return the instance on success, None on failure.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)

            if not isinstance(obj, cls):
                return None
            return obj
        except (
            FileNotFoundError,
            EOFError,
            OSError,
            pickle.UnpicklingError,
            pickle.PickleError,
        ):
            return None
