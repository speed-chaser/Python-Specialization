from sqlalchemy import Column, create_engine
from sqlalchemy.types import String, Integer
from sqlalchemy.ext.declarative import declarative_base

# Create an SQLAlchemy engine
engine = create_engine('mysql://cf-python:password@localhost/my_database', echo=True)

# Create a base class
Base = declarative_base()

del Recipe

# This should match the existing table definition
class Recipe(Base):
    __tablename__ = "practice_recipes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + " (New __repr__)>"