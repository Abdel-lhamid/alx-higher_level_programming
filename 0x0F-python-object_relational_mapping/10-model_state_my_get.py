#!/usr/bin/python3
"""
prints the State object with the name passed as arg from the db hbtn_0e_6_usa
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
    res = session.query(State).filter_by(State.name=argv[4]).first()
    # print
    if res:
        print(res[0].id)
    else:
        print("Not found")
