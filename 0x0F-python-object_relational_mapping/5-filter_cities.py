#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv
from exec_query import execquery

if __name__ == "__main__":
    if len(argv) != 5:
        exit(1)
    query = """SELECT cities.name FROM cities
               INNER JOIN states ON states.id=cities.state_id
               WHERE states.name = %s ORDER BY cities.id ASC"""
    res = execquery("localhost",
                    3306, argv[1],
                    argv[2], argv[3], query, (argv[4], ))
    # print
    print(', '.join(["{:s}".format(row[0]) for row in res]))
