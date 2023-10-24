#!/usr/bin/python3
"""
python file contains class definit of City and Base = declarative_base():
City class: inherits from Base Tips; links to the MySQL table states
class attr id represents a column of an auto-generated, unique integer,
can’t be null and is a primary key
class attr name represents a column of string w/ max 128 chars and not null
class attr state_id represents a column of an integer, can’t be null and 
is a foreign key to states.id
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from model_state import Base, State


class City(Base):
    """inherit from Base, City is an ORM class, links to table cities"""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
