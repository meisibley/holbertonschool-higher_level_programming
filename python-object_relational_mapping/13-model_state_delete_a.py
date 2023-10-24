#!/usr/bin/python3
"""deletes all State objects w/ name contains 'a' from db hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    new_session = sessionmaker(bind=engine)
    session = new_session()

    del_state = session.query(State)
    for state in del_state:
        if 'a' in state.name:
            session.delete(state)
    session.commit()
    session.close()
