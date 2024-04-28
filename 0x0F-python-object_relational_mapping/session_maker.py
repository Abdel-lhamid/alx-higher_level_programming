#!/usr/bin/python3
"""
reusable function to create engin and return a session
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def make_session(user, passwd, db):
    """
    make engine and create session
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    return(Session())
