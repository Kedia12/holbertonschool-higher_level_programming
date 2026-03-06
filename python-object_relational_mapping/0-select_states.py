#!/usr/bin/python3
"""
Module that list all states from a database.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Connects to the MySQL database and retrieves all states.
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
