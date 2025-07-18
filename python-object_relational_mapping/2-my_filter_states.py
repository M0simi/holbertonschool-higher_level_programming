#!/usr/bin/python3
"""
Lists states from the database hbtn_0e_0_usa
that start with a given name (case-sensitive).
Usage: ./script.py <username> <password> <database> <state name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306,
    )
    cursor = db.cursor()
    query = """
        SELECT * FROM states
        WHERE name LIKE BINARY '{}%'
        ORDER BY id ASC
    """.format(
        sys.argv[4]
    )
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
