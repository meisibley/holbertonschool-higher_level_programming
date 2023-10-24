#!/usr/bin/python3
"""
    Write a python file that contains the class definition of
    a City and an instance Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """inherits from Base Tips and links to the MySQL table cities"""

    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
