#!/usr/bin/python3
"""Class definition of a State and an instance."""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb
import sys


Base = declarative_base()


class State(Base):
    """Class that displays state in the database."""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    db = MySQLdb.connect
