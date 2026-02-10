#!/usr/bin/env python3
"""Basic: serialize and deserialize a dictionary to JSON files."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary and save it to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load a JSON file and deserialize it into a dictionary."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
