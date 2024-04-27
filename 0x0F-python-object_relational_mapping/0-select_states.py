#!/usr/bin/python3
"""
select all states from the table states on the given db
"""


import MySQLdb
from sys import argv
from exec_query import execquery

if __name__ == "__main__":

    query = "SELECT * FROM states ORDER BY id ASC"
    res = execquery("localhost",
                    3306, argv[1],
                    argv[2], argv[3], query)
    # print
    for row in res:
        print(row)
