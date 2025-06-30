#!/usr/bin/python3
"""
Script to list all states starting with 'N' from a MySQL database
Usage: ./1-filter_states.py <username> <password> <database_name>
"""

import MySQL
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=db_name
    )

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
