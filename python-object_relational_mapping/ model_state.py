#!/usr/bin/python3
"""
Class definition of a State and an instance
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
    
class State (Base):
    """
    class that display state in the database
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# engine = create_engine("mysql+mysqldb://user:password@localhost:3306/database_name")
# Base.metadata.create_all(engine)
