import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import session
import datetime

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, Float, ForeignKey

class CategoryModel(Base):
	__tablename__ = "Category"
	category_id = Column(Integer, primary_key=True)
	name = Column(String)
	details = Column(String)
	Item = relationship("Item", back_populates ="category")

	def __str__(self):
		return 'CategoryModel(category_id={},name ={}, details={})'.format(self.category_id, self.details)

class ItemModel(Base):
	__tablename__ = "Item"
	item_id = Column(Integer, primary_key=True)
	name = Column(String)
	details = Column(String)
	unit_price = Column(Float)
	total = Column(Float)
	date_added = Column(DateTime,default=datetime.datetime.now)
	status = Column(Boolean)
	category_id = Column(Integer, ForeignKey('Category.category_id'))
	CategoryModel = relationship("Category", back_populates ="Item")

	def __str__(self):
		return 'ItemModel(item_id={}, name={}, details={}, unit_price={}, total={}, date_added={}, status={})'.format(self.item_id, self.name, self.details, self.unit_price, self.total, self.date_added, self.status)

engine = create_engine('sqlite:///inventory.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine 

   