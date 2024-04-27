#!/usr/bin/python3
"""
select all states from the table states on the given db
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    # create db connection
    db = MySQLdb.connect(host="localhost",
                         port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    # cursor
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    res = cursor.fetchall()
    # print
    for row in res:
        print(row)

    cursor.close()
    db.close()
