import sqlalchemy
from sqlalchemy import create_engine
import datetime

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, Float, ForeignKey

class InventoryModel(Base):
	__tablename__ = "Category"
	item_id = Column(Integer, primary_key=True)
	name = Column(String)
	details = Column(String)
	quantity = Column(String)
	unit_price = Column(Float)
	total = Column(Float)

	__tablename__ = "Item"
	serial_id =Column(Integer, primary_key=True)
	item_id = Column(Integer)
	date_added = Column(DateTime,default=datetime.datetime.now)
	status = Column(Boolean)

engine = create_engine('sqlite:///inventory.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine 

   