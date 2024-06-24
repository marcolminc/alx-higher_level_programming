#!/usr/bin/python3
"""
    Defines a State Class and an instance of Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """
        State class that links to MySQL table 'states'
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    if __name__ == "__main__":
        engine = create_engine('mysql://username:password@localhost:3306/database_name')
        #crate tables in the db(defined by Base's subclasses)
        Base.metadata.create_all(engine)
