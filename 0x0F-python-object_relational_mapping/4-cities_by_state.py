#!/usr/bin/python3
""" This module connects to a MySQL server and lists all
states that match a specified name in argv. """


if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states INNER JOIN " +
                   "cities ON states.id = cities.state_id" +
                   "ORDER BY cities.id ASC")

    results = cursor.fetchall()

    for row in results:
        print("(" + str(row[2]) + ", '" + str(row[4]) +
              "', '" + str(row[1]) + "')")

    db.close()
