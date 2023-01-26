import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
# //clase=molde objetos=galletitas
# class(creo molde) person=el nombre q le pongo 
class Usuario(Base):
    __tablename__ = 'usuario'#aca si puedo poner en minus
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    #nombre=columna(entero,es una clave primaria ) esto es pa crear columnas
    id = Column(Integer, primary_key=True)
    #nombre=clumna(tipo de dato que va a ir, si acepta campos vacios o no)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Planetas(Base):
    __tablename__ = 'planetas'#aca si puedo poner en minus
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    #nombre=columna(entero,es una clave primaria ) esto es pa crear columnas
    id = Column(Integer, primary_key=True)
    #nombre=clumna(tipo de dato que va a ir, si acepta campos vacios o no)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)


class Vehiculos(Base):
    __tablename__ = 'vehiculos'#aca si puedo poner en minus
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    #nombre=columna(entero,es una clave primaria ) esto es pa crear columnas
    id = Column(Integer, primary_key=True)
    #nombre=clumna(tipo de dato que va a ir, si acepta campos vacios o no)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)


class Personajes(Base):
    __tablename__ = 'personajes'#aca si puedo poner en minus
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    #nombre=columna(entero,es una clave primaria ) esto es pa crear columnas
    id = Column(Integer, primary_key=True)
    #nombre=clumna(tipo de dato que va a ir, si acepta campos vacios o no)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)




class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id= Column(Integer, ForeignKey('usuario.id'))
    personajes_id= Column(Integer, ForeignKey('personajes.id'))
    planetas_id= Column(Integer, ForeignKey('planetas.id'))
    vehiculos_id= Column(Integer, ForeignKey('vehiculos.id'))
   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
