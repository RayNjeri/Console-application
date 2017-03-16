import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import session
import datetime

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, Float, ForeignKey

class CategoryModel(Base):
	__tablename__ = "category"
	category_id = Column(Integer)
	name = Column(String, primary_key=True)
	details = Column(String)
	itemModel = relationship("ItemModel", backref ="category")

	def __str__(self):
		return 'CategoryModel(category_id={},name ={}, details={})'.format(self.category_id, self.details)

class ItemModel(Base):
	__tablename__ = "Item"
	item_id = Column(Integer, primary_key=True)
	name = Column(String)
	details = Column(String)
	unit_cost = Column(Float)
	quantity =Column(Float)
	total = Column(Float)
	date_added = Column(DateTime,default=datetime.datetime.now)
	status = Column(Boolean)
	category_id = Column(Integer, ForeignKey('category.name'))
	categoryModel = relationship("CategoryModel", backref ="Item")

	def __str__(self):
		return 'ItemModel(item_id={}, name={}, details={}, unit_cost={}, quantity={}, total={}, date_added={}, status={})'.format(self.item_id, self.name, self.details, self.unit_cost, self.quantity, self.total, self.date_added, self.status)

engine = create_engine('sqlite:///inventory.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine 

   