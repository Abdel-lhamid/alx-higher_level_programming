#!/usr/bin/python3
"""
reusable function to create engin and return a session
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base


def make_session(user, passwd, db):
    """
    make engine and create session
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return(Session())
