#!/usr/bin/python3
""" This module all objects are listed from the ORM """

if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy.ext.declarative import declarative_base
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("mysql://{}:{}@localhost/{}".
                           format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    q = session.query(State).order_by(State.id).filter(State.name == argv[4]).first()
    if q:
        print(str(q.id))
    else:
        print('Not found')
