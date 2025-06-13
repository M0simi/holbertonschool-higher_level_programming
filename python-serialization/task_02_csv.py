#!/usr/bin/python3
"""
Module: task_02_csv

This module provides a function to convert CSV data to JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts the contents of a CSV file to a JSON file named 'data.json'.

    Args:
        csv_filename (str): The path to the CSV file to be converted.

    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    try:
        # Open the CSV file and read rows as dictionaries
        with open(csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        # Serialize and write to JSON file
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        # If the CSV file doesn't exist
        return False

    except Exception as e:
        # Catch-all for any other errors
        return False
