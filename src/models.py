import os
import sys
from sqlalchemy import Integer
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Characters(Base):
    __tablename__ = 'characters'
    name = Column(String(250), ForeignKey('vehicle.pilot'), ForeignKey('favorites.favorite_characters') )
    planet_from = Column(String(250), ForeignKey('planets.name'))
    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    size = Column(Integer)  
    population = Column(Integer)
    climate = Column(String(250))
    name = Column(String(250), ForeignKey('favorites.favorite_planets'))

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), ForeignKey('favorites.favorite_vehicles'))
    pilot = Column(String(250))
    type = Column(String(250))

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, ForeignKey('favorites.user_id'), primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    
class Favorites(Base):
    __tablename__ = 'favorites'
    date_added = Column(DateTime(False))
    user_id = Column(Integer, primary_key=True)
    favorite_characters = Column(String(250))
    favorite_planets = Column(String(250))
    favorite_vehicles = Column(String(250))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')




