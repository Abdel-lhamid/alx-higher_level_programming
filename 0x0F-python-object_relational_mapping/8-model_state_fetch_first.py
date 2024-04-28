#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from session_maker import make_session
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    # use make_session func to get the session()
    session = make_session(argv[1], argv[2], argv[3])

    # query python instances in database
    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print("{:d}: {:s}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
