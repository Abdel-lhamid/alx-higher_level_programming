#!/usr/bin/python3
"""
Defines class City
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state() import Base, State

Base = declarative_base()


class City(Base):
    """
    Class State; instance of Base
    Linked to MySQL table "states"
    """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128),  nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
