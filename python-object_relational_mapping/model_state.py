#!/usr/bin/python3
"""
python file contains class definit of State and Base = declarative_base():
State class: inherits from Base Tips; links to the MySQL table states
class attr id represents a column of an auto-generated, unique integer,
can’t be null and is a primary key
class attr name represents a column of string w/ max 128 chars and not null
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """inherit from Base, State is an ORM class"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
