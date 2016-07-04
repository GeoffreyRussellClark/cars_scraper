
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, Integer, String, DateTime

import settings

DeclarativeBase = declarative_base()

def db_connect():
	"""
	performs database connection using database settings from settings.py
	returns sqlalchemy engine instance
	"""
	return create_engine(URL(**settings.DATABASE))

def create_cars_table(engine):
	DeclarativeBase.metadata.create_all(engine)
	
class Cars(DeclarativeBase):
	"""Sqlalchemy Cars model"""
	__tablename__ = "newcars_carscoza"
	
	id = Column(Integer, primary_key=True)
	make = Column('make',String)
	model = Column('model',String)
	version = Column('version', String)
	price = Column('price', String)
	curr_date = Column('curr_date',String)
	'''intro_date = Column('intro_date', String, nullable=True)
    model_intro_date = Column('model_intro_date', String, nullable=True)
    sa_intro_date = Column('sa_intro_date', String, nullable=True)
    fuel_consumption = Column('fuel_consumption', String, nullable=True)
    engine_capacity = Column('engine_capacity', String, nullable=True)
    engine_size = Column('engine_size', String, nullable=True)
    engine_location = Column('engine_location', String, nullable=True)
    cylinders = Column('cylinders', String, nullable=True)
    power_max = Column('power_max', String, nullable=True)
    torque_max = Column('torque_max', String, nullable=True)
    transmission = Column('transmission', String, nullable=True)
    abs_brakes = Column('abs_brakes', String, nullable=True)
    acceleration_0to100 = Column('acceleration_0to100', String, nullable=True)
    top_speed = Column('top_speed', String, nullable=True)
    airbags = Column('airbags', String, nullable=True)
    fuel = Column('fuel', String, nullable=True)
    doors = Column('doors', String, nullable=True)
    seats = Column('seats', String, nullable=True)
    body_shape = Column('body_shape', String, nullable=True)
    driven_wheels = Column('driven_wheels', String, nullable=True)
    gears = Column('gears', String, nullable=True)
    length = Column('length', String, nullable=True)
    width = Column('width', String, nullable=True)
    weight = Column('weight', String, nullable=True)
    load_volume_capacity = Column('load_volume_capacity', String, nullable=True)
    load_carrying_capacity = Column('load_carrying_capacity', String, nullable=True)
    fuel_capacity = Column('fuel_capacity', String, nullable=True)
    warranty_distance = Column('warranty_distance', String, nullable=True)
    service_plan_distance = Column('service_plan_distance', String, nullable=True)
    service_interval_distance = Column('service_interval_distance', String, nullable=True)'''
