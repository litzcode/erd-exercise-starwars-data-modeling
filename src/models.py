import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    lastname = Column(String(50))
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    fav_characters = relationship("Fav_Character", back_populates="user") # One to Many. One user can have many fav_character
    fav_planets = relationship("Fav_Planet", back_populates="user") # One to Many. One user can have many fav_planet

    # Defining a method inside the class is OPTIONAL
    # The %s operator lets you add a value into a Python string
    def serialize(self):
        return "<User(name='%s', lastname='%s', username='%s')>" % (self.name, self.lastname, self.username)


class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    hair_color = Column(String(50), nullable=False)
    fav_character = relationship("Fav_Character", uselist=False, back_populates="character") # One to One. One character is associated with One fav_character.id

class Fav_Character(Base):
    __tablename__ = "fav_character"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id")) # One to Many. One user can have many favorites
    character_id = Column(Integer, ForeignKey("character.id")) # One to One. One character is associated with One fav_character.id
    character = relationship("Character", back_populates="fav_character") # One to One. One character is associated with One fav_character.id


class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)
    fav_planet = relationship("Fav_Planet", uselist=False, back_populates="planet") # One to One. One planet is associated with One fav_planet.id

class Fav_Planet(Base):
    __tablename__ = "fav_planet"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id")) # One to Many. One user can have many favorites
    planet_id = Column(Integer, ForeignKey("planet.id")) # One to One. One planet is associated with One fav_planet.id
    planet = relationship("Planet", back_populates="fav_planet") # One to One. One planet is associated with One fav_planet.id


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')