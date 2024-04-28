#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
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
    for instance in session.query(State).order_by(State.id):
        print("{:d}: {:s}".format(instance.id, instance.name))
