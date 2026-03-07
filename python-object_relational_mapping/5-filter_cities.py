#!/usr/bin/python3
"""A script that the argument and lists all cities."""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    }

    cursor = database.cursor()

    cursor.execute("""
                   SELECT cities.id, cities.name, states.name
                   FROM citiess JOIN states
                   ON cities.state_id = states.id
                   ORDER BY cities.id
                   """, (sys.argv[4],)
    )

    for row in curl.fetchall():
        print(row)

    cur.close()
    db.close()
