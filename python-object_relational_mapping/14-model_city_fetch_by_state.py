#!/usr/bin/python3
"""Write a script that prints all City objects"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()
    combo_sess = sess.query(City, State).\
        filter(City.state_id == State.id).all()
    for city, state in combo_sess:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
