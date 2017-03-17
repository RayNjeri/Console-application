from IMA import CategoryModel, ItemModel
from sqlalchemy.orm import Session
import datetime
import sqlite3
import csv
session = Session()

class Products:
    def get_Item_Category(self):
      categories= session.query(CategoryModel).all()
      for category in categories:
        print("{} {}".format(category.name, category.details))
      category = input('Which Category?')
      return category

    def create_category(self, name, details):
        category = CategoryModel(name=name, details=details)
        session.add(category)
        session.commit()
        print("category successfully created")
    
    def update_category(self, name, item):

       category= session.query(CategoryModel).filter_by(name = name).first()
       if category:
        category.name = name
        category.details = item
        session.commit()
        print('Category successfully updated.') 
       else:
          print('Category not found')
  
        
    def delete_category(self, name):
      category = session.query(CategoryModel).filter_by(name= name).first()
      if category:
        session.delete(category)
        session.commit()
        print('Category successfully deleted.')
      else:
          print("Category not found")

    def view_category(self, name):
        category = session.query(CategoryModel).filter_by(name=name).one();
        if category:
            print(category.details)
        else:
            print("Category does not exist")

    def search_category(self, name):
      try:

         category = session.query(CategoryModel).filter(CategoryModel.name.like('%' + name + '%'))
         if category:
            for category in category:
                print(category.name)
         else:
            print("Category not found")
      except Exception as e:
        print(str(e))
    

class Particulars:
    def get_items_Item():
        items= sesssion.query(CategoryModel).all()
        for item in categories:
            print("{} {}".format(item.name, item.details, item.unit_cost, quantity, item.total, item.date_added, item.status))
            item_id = input('Which item?')
            return int(item_id)

    def create_item(self, name, details, unit_cost, quantity, total, status, category_id):
        item = ItemModel(name=name, details=details, unit_cost =unit_cost, quantity =quantity, total =total, status =status, date_added =datetime.datetime.now(), category_id =category_id)
        session.add(item)
        session.commit()

    def update_item(self, name):
      item = session.query(ItemModel).filter_by(name = name).first()
      if item:
        item.name = name
        session.commit()
        print('item successfully updated.') 
      else:
        print('item not found')
       

    def delete_item(self, name):
       item = session.query(ItemModel).filter_by(name= name).first()
       if item:
        session.delete(item)
        session.commit()
        print('item successfully deleted.')
       else:
        print("item not found")

    def view_item(self, name):
       category = session.query(ItemModel).filter_by(name=name).one();
       if item:
        print(item.details)
       else:
        print("Category does not exist")
        

    def search_item(self, name):
       try:

         category = session.query(ItemModel).filter(ItemModel.name.like('%' + name + '%'))
         if item:
            for item in item:
                print(item.name)
         else:
            print("item not found")

       except Exception as e:
         print(str(e))
    
        
     
    def asset_value(self, quantity, unit_cost):
        items= sesssion.query(CategoryModel).all()
        x = session.query.filter_by(name = name).first
        return x
        y = session.query.filter_by(unit_cost= unit_cost).first
        return y
        asset_value = item.total
        total = x*y
        return total 




              

