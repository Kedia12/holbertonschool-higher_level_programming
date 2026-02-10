#!/usr/bin/env python3
"""Serialize and deserialize Python dictionaries using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary into an XML file."""
    root = ET.Element('data')  # racine <data>

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # convertit tout en string

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize an XML file back into a Python dictionary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data = {}
        for child in root:
            data[child.tag] = child.text  # tout sera string
        return data
    except (ET.ParseError, FileNotFoundError):
        return None
