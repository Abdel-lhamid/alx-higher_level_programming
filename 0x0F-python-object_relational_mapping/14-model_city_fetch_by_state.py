#!/usr/bin/python3
"""
lists all cities objects from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from session_maker import make_session
from model_state import Base, State
from model_city import City
from sys import argv


if __name__ == "__main__":
    # use make_session func to get the session()
    session = make_session(argv[1], argv[2], argv[3])

    # query python instances in database
    res = session.query(State.name, City.id, City.name).filter(
            State.id == City.state_id).order_by(State.id)
    for r in res:
        print("{:s}: ({:d}) {:s}".format(r[0], r[1], r[2]))
