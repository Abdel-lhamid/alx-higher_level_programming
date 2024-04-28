#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the db hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from session_maker import make_session
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    # use make_session func to get the session()
    session = make_session(argv[1], argv[2], argv[3])

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
