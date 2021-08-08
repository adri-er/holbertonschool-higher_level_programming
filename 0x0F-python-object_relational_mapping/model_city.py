#!/usr/bin/python3
""" This module defines Base Class for a City and makes
it a declarative base. """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """ Defines  a table for cities in the US """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'), nullable=False)
    name = Column(String(128), nullable=False)
