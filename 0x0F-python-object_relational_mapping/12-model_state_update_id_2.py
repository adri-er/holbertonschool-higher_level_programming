#!/usr/bin/python3
""" This module all objects are listed from the ORM """

if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy.ext.declarative import declarative_base
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("mysql://{}:{}@localhost/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)

    session = Session()

    state_change = session.query(State).filter_by(id='2').first()
    state_change.name = 'New Mexico'
    session.commit()
