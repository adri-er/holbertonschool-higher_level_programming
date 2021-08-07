#!/usr/bin/python3
""" This module connects to a MySQL server and lists all
states that match a specified name in argv. """
if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name = %s", (sys.argv[4], ))

    results = cursor.fetchall()

    for row in results:
        print ("(" + str(row[0]) + ", '" + str(row[1]) + "')")

    db.close()
