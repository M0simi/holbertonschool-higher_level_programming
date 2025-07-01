#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
Each city is displayed with its id, name, and state name.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database using command-line arguments
    db = MySQLdb.connect(
        user=sys.argv[1],  # MySQL username
        password=sys.argv[2],  # MySQL password
        database=sys.argv[3],  # Database name
        port=3306,  # Default MySQL port
    )

    query = db.cursor()

    # Execute a single SQL query to retrieve all cities with their state names
    query.execute(
        """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    )

    # Fetch all results from the executed query
    rows = query.fetchall()

    for row in rows:
        print(row)
