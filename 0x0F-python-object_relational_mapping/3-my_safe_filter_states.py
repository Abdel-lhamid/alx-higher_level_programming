#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv
from exec_query import execquery

if __name__ == "__main__":
    if len(argv) != 5:
        exit(1)
    query = """SELECT * FROM states
               WHERE name = %s ORDER BY id ASC"""
    res = execquery("localhost",
                    3306, argv[1],
                    argv[2], argv[3], query, (argv[4], ))
    # print
    for row in res:
        print(row)
