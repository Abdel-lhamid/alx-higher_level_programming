#!/usr/bin/python3
"""
deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from session_maker import make_session
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    # use make_session func to get the session()
    session = make_session(argv[1], argv[2], argv[3])
    res = session.query(State).filter(State.name.like('%a%')).all()
    for s in res:
        session.delete(s)

    session.commit()
