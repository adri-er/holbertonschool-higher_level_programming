#!/usr/bin/python3
""" This module all objects are listed from the ORM """

if __name__ == "__main__":
    from model_city import Base, City
    from model_state import Base, State
    from sqlalchemy.ext.declarative import declarative_base
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("mysql://{}:{}@localhost/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)

    session = Session()

    query_sc = session.query(State.name.label('state__name'),
                             State.id.label('state__id'),
                             City.id.label('city_id'),
                             City.name.label('city_name')
                             ).join(City, State.id == City.state_id)
    for state_city in query_sc.order_by(City.id):
        print(state_city.state__name + ": " + "(" + str(state_city.city_id) +
              ") " + state_city.city_name)
