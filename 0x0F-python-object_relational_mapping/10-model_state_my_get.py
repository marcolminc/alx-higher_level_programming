#!/usr/bin/python3
"""
Module that retrieves and prints the very first state
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    user = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, pwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    match = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print('{}'.format(state.id))
            match = True
            break

    if match is False:
        print('Not found')
