#!/usr/bin/python3
"""Print the first State object from the database hbtn_0e_6_usa."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main():
    """Define the main function"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}'
                           '@localhost:3306/{}'.format(username, password,
                                                       database))
    session = sessionmaker(bind=engine)
    session = session()
    states = session.query(State).order_by(State.id).first()
    if states:
        print("{}: {}".format(states.id, states.name))
    else:
        print("Nothing")
    session.close()


if __name__ == "__main__":
    main()
