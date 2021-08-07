#!/usr/bin/python3
""" This module connects to a MySQL server and lists all
states from a database. """
if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])

    cursor = db.cursor()

    sql = "SELECT * FROM states ORDER BY id ASC"

    cursor.execute(sql)

    results = cursor.fetchall()

    printed = []
    for row in results:
        if (row[1][0] == 'N' and row[1] not in printed):
            print ("(" + str(row[0]) + ", '" + str(row[1]) + "')")
            printed.append(row[1])

    db.close()
