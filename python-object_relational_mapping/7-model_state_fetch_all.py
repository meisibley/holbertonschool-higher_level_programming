#!/usr/bin/python3
"""Write a script that lists all State objects from the db hbtn_0e_6_usa"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    new_session = sessionmaker(bind=engine)
    session = new_session()
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        session.close()
