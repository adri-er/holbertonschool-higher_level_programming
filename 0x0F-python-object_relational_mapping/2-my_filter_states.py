#!/usr/bin/python3
""" This module connects to a MySQL server and lists all
states from a database with specified name in argv. """


if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])

    cursor = db.cursor()

    sql = "SELECT * FROM states " +
    "WHERE name=\'{}\' ORDER BY id".format(sys.argv[4])

    cursor.execute(sql)

    results = cursor.fetchall()

    for row in results:
        print("(" + str(row[0]) + ", '" + str(row[1]) + "')")

    db.close()
