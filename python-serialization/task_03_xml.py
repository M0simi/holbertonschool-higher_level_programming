#!/usr/bin/python3
"""
This module provides functions to serialize and deserialize Python dictionaries using XML format.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the output XML file.

    Returns:
        None
    """
    try:
        # Create the root element
        root = ET.Element("data")

        # Add each key-value pair as a child element
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)  # Convert value to string for XML compatibility

        # Build the tree and write it to the file
        tree = ET.ElementTree(root)
        tree.write(filename)
    except Exception as e:
        print(f"Error during serialization: {e}")


def deserialize_from_xml(filename):
    """
    Deserializes an XML file back into a Python dictionary.

    Args:
        filename (str): The name of the XML file to read from.

    Returns:
        dict: The reconstructed dictionary, or None if there's an error.
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Construct a dictionary from the XML elements
        result = {}
        for child in root:
            result[child.tag] = child.text

        return result
    except Exception as e:
        print(f"Error during deserialization: {e}")
        return None
