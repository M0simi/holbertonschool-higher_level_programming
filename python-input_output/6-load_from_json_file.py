#!/usr/bin/python3
"""
This module defines a function that
create an object from a JSON fole
"""

import json


def load_from_json_file(filename):
    """create an object from a JSON file"""
    with open(filename, "r") as f:
        return json.load(f)
