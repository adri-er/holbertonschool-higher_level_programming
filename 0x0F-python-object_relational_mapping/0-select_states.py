#!/usr/bin/python3
"""
This module connects to a MySQL server and lists all
states from a database.
"""
import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])

    cursor = db.cursor()

    sql = "SELECT * FROM states ORDER BY id ASC"

    cursor.execute(sql)

    results = cursor.fetchall()

    for row in results:
        print("(" + str(row[0]) + ", '" + str(row[1]) + "')")

    db.close()
