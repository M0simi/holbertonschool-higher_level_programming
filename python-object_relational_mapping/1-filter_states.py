#!/usr/bin/python3
"""
List all states from the database hbtn_0e_0_usa
that start with an uppercase 'N'.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Read credentials from command line arguments
    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name,
        charset="utf8",
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Select states starting with 'N' (case-sensitive)
    cursor.execute(
        """
        SELECT * FROM states
        WHERE name LIKE 'N%'
        ORDER BY id ASC
    """
    )

    # Fetch and print all matching rows
    for row in cursor.fetchall():
        print(row)

    # Clean up
    cursor.close()
    db.close()
