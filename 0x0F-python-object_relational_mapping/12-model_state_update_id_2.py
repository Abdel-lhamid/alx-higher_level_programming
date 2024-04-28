#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_usa
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
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"

    session.commit()
