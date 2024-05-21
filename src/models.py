import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class FavoriteEnum(enum.Enum):
    PLANET = 'planet'
    CHARACTER = 'character'

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    image = Column(String(500), nullable=True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    is_favorite = Column(Boolean, default=False)
    climate = Column(String(50))
    population = Column(Integer)
    terrain = Column(String(50))
    image = Column(String(250))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(100), nullable=False)
    is_favorite = Column(Boolean, default=False)
    age = Column(Integer, nullable=False)
    image = Column(String(250))
    birth_year = Column(String(10))
    eye_color = Column(String(10))
    gender = Column(String(10))
    hair_color = Column(String(20))
    homeworld = Column(String, ForeignKey('planet.name'))

    planet = relationship(Planet)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    favorite_enum = Column(Enum(FavoriteEnum))

    user = relationship(User)
    character = relationship(Character)
    planet = relationship(Planet)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
