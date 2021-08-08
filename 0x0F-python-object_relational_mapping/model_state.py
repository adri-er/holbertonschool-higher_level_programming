#!/usr/bin/python3
"""
This module defines Base Class for a State and makes
it a declarative base.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Defines a table with states of the US """
    __tablename__ = 'states'


    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
