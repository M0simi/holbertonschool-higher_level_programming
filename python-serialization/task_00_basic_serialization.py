#!/usr/bin/python3
"""
Module: task_00_basic_serialization

This module provides two functions to perform basic serialization and
deserialization of Python dictionaries using JSON format.

Functions:
- serialize_and_save_to_file(data, filename): Saves adictionary to a JSON file.
- load_and_deserialize(filename): Loads a dictionary from a JSON file.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to JSON and saves it to a file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The name of the file where the JSON data will be saved.

    Notes:
        - If the file already exists, it will be overwritten.
        - Uses UTF-8 encoding by default.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_and_deserialize(filename):
    """
    Loads JSON data from a file and deserializes
    it back into a Python dictionary.

    Args:
        filename (str): The name of the file containing the JSON data.

    Returns:
        dict: The deserialized Python dictionary.

    Notes:
        - Assumes that the file contains valid JSON.
        - Uses UTF-8 encoding by default.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
