#!/usr/bin/python3
"""
 script that lists all cities from the database hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv
from exec_query import execquery

if __name__ == "__main__":
    if len(argv) != 4:
        exit(1)
    query = """SELECT cities.id, cities.name, states.name FROM
               cities INNER JOIN states ON states.id=cities.state_id"""
    res = execquery("localhost",
                    3306, argv[1],
                    argv[2], argv[3], query)
    # print
    for row in res:
        print(row)
