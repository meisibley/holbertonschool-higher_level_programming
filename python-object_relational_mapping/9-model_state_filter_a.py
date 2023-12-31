#!/usr/bin/python3
"""script lists all State objects contain letter a from db hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    new_session = sessionmaker(bind=engine)
    session = new_session()
    for state in session.query(State).filter(State.name.like('%a%')).\
            order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
