
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
	
	__tablename__ = "newcars_carscoza"
	
	id = Column(Integer, primary_key=True)
	make = Column('make',String)
	model = Column('model',String)
	version = Column('version', String)
	price = Column('price', String)
	curr_date = Column('curr_date',DateTime)
	f1name = Column('f1name',String)
	f1value = Column('f1value',String)
	f2name = Column('f2name',String)
	f2value = Column('f2value',String)
	f3name = Column('f3name',String)
	f3value = Column('f3value',String)
	f4name = Column('f4name',String)
	f4value = Column('f4value',String)
	f5name = Column('f5name',String)
	f5value = Column('f5value',String)
	f6name = Column('f6name',String)
	f6value = Column('f6value',String)
	f7name = Column('f7name',String)
	f7value = Column('f7value',String)
	f8name = Column('f8name',String)
	f8value = Column('f8value',String)
	f9name = Column('f9name',String)
	f9value = Column('f9value',String)
	f10name = Column('f10name',String)
	f10value = Column('f10value',String)
	f11name = Column('f11name',String)
	f11value = Column('f11value',String)
	f12name = Column('f12name',String)
	f12value = Column('f12value',String)
	f13name = Column('f13name',String)
	f13value = Column('f13value',String)
	f14name = Column('f14name',String)
	f14value = Column('f14value',String)
	f15name = Column('f15name',String)
	f15value = Column('f15value',String)
	f16name = Column('f16name',String)
	f16value = Column('f16value',String)
	f17name = Column('f17name',String)
	f17value = Column('f17value',String)
	f18name = Column('f18name',String)
	f18value = Column('f18value',String)
	f19name = Column('f19name',String)
	f19value = Column('f19value',String)
	f20name = Column('f20name',String)
	f20value = Column('f20value',String)
	
	
