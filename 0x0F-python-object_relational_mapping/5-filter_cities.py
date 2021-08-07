#!/usr/bin/python3
""" This module connects to a MySQL server and lists all
states that match a specified name in argv. """


if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states INNER JOIN " +
                   "cities ON states.id = cities.state_id " +
                   "WHERE states.name LIKE \'{}\'". format(sys.argv[4]) +
                   " ORDER BY cities.id ASC")

    results = cursor.fetchall()

    for i in range(len(results)):
        print(str(results[i][4]), end='')
        if i != (len(results) - 1):
            print(", ", end='')
        else:
            print("")

    db.close()
