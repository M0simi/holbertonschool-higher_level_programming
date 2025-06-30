#!/usr/bin/python3
"""
Script to list all states from a MySQL database
Usage: ./0-select_states.py <username> <password> <database_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=db_name
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
