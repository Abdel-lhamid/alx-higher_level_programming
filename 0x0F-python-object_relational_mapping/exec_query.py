#!/usr/bin/python3
"""
select all states from the table states on the given db
"""


import MySQLdb


def execquery(host1, port1, user1, passwd1, db1, query, params=None):
    # create db connection
    db = MySQLdb.connect(host=host1,
                         port=port1, user=user1,
                         passwd=passwd1, db=db1)
    # cursor
    cursor = db.cursor()
    cursor.execute(query, params)
    res = cursor.fetchall()

    cursor.close()
    db.close()
    return(res)
