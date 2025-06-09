#!/usr/bin/python3
"""
This module defines a function that
return string representation of an JSON.
"""

import json


def from_json_string(my_str):
    """return fron json to string"""
    return json.loads(my_str)
