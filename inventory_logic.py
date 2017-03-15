from IMA import InventoryModel
from sqlalchemy.orm import Session
session = Session()

class Inventory:
	def __init__(self, name, details, quantity, unit_price, total, status, date_added):
		self.name = name
		self.details = details
		self.quantity = quantity
		self.unit_price = unit_price
		self.total = total
		self.status = status
		self.date_added = date_added


	def create_category(self, name, details, quantity, unit_price, total):
		category = InventoryModel(name =name, details =details, quantity =0, unit_price =unit_price, total =total)
		session.add(category)
		session.commit()

	def create_item(self, serial_id, item_id, date_added,status):
		item = InventoryModel(serial_id =serial_id, date_added =date_added, status= status )
		quantity = increment_quantity(item_id)
		session.add(item)
		session.commit()



	def update_category(self, name, details, quantity, unit_price, total, status):
		category = InventoryModel.query.filter_by(item_id =item_id)
		if item:
			item_id = item_id
			session.update(category)
			session.commit()
		else:
			print("ITEM NOT fOUND")


	def update_item(self, serial_id, item_id, date_added, status):
		item = InventoryModel.query.filter_by(serial_id =serial_id)
		if item:
			serial_id= item_id
			session.update(item)
			session.commit()
		else:
			print("ITEM NOT fOUND")

		
	def delete_category(self, name, details, quantity,  unit_price, total):
		item = InventoryModel.query.filter_by(item_id = item_id)
		if item:
			item_id = ray
			session.delete(item)
		else:
			print("ITEM NOT FOUND")

	def delete_item(self, serial_id, item_id, date_added, status):
		item = InventoryModel.query.filter_by(serial_id = serial_id)
		if item:
			serial_id = serial_id
			session.delete(item)
		else:
			print("ITEM NOT FOUND")

	def view_category(self, name, details, quantity, unit_price, total):
		for instance in session.query(category).order_by(item_id):
			print(instance.name, instance.details, instance.unit_price, instance.total)

	def view_item(self,serial_id, item_id, date_added,status):
		for instance in session.query(item).order_by(serial_id):
			print(instance.serial_id, instance.date_added, instance.status)

	
	def increment_quantity():
		while item_id.item == item_id.category:
			return quantity.category += 1
			session.commit()


	def decrement_quanity():
		while item_id.category == item_id.item:
			return quantity.category -= 1
			session.commit()

	def check_in_out():
		if item.status == checked InventoryModel:
			return true

		else:
			return false:


    def search_query_category():
    	for instance in session.query(category).order_by(item_id, name, details, unit_price):
    		print(instance.item_id, instance.name, instance.details, instance.unit_price)


   	def search_query_item():
   		for instance in session.query(item).order_by(serial_id, status):
   			print(instance.serial_id, instance.status)






