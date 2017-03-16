from IMA import CategoryModel, ItemModel
from sqlalchemy.orm import Session
import datetime
session = Session()

class Products:
    def get_Item_Category(self):
      categories= sesssion.query(CategoryModel).all()
      for category in categories:
        print("{} {}".format(category.name, category.details))
        category_id = input('Which Category?')
      return int(category_id)

    def create_category(self, name, details):
        category = CategoryModel(name=name, details=details)
        session.add(category)
        session.commit()
    
    def update_category(self, name):
       categories= session.query(CategoryModel).all()
       print('select which category to update')
       category_id = get_Item_Category()
       category = input('enter field to update')
       category_id = session.query.filter_by(name= name).one()
       if not category:
         print('Category not found')
       else:
        new_content = input('Enter new category: ')
        category.category_id = new_content
        session.commit()
        print('Category successfully updated.')

    def delete_category(self, name, details):
      categories= session.query(CategoryModel).all()
      print('select which category to Delete')
      category_id = get_Item_Category()
      category = input('enter field to Delete')
      category_id = session.query.filter_by(name= name).one()
      if not category:
         print('Category not found')
      else:
        category.delete_category
        session.commit()
        print('Category successfully deleted.')

    def view_category(self, name,details):
        category = session.query(CategoryModel).filter_by(name=name).one();
        print(category)

    def search_category(self, name,details):
        category = session.query(CategoryModel).filter_by(name=name).one();
        print(category)
    

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
       items= session.query(CategoryModel).all()
       print('select which item to update')
       item_id = get_items_Item
       item = input('enter field to update')
       item_id = session.query.filter_by(name= name).one()
       if not item:
         print('item not found')
       else:
        new_content = input('Enter new item: ')
        item.item_id = new_content
        session.commit()
        print('item successfully updated.')

    def delete_item(self, name):
        item= session.query(ItemModel).all()
        print('select which item to Delete')
        item_id = get_items_Item
        item = input('enter field to Delete')
        item_id = session.query.filter_by(name= name).one()
        if not item:
            print('item not found')
        else:
            item.delete_item
            session.commit()
            print('item successfully deleted.')

    def view_item(self, name,details, unit_cost,quantity, total,status,date_added):
        item = session.query(ItemModel).filter_by(name=name).one();
        print(item)

    def search_item(self, name):
        item = session.query(ItemModel).filter_by(name=name).one();
        print(item)
     
    def asset_value(self, quantity, unit_cost):
        items= sesssion.query(CategoryModel).all()
        x = session.query.filter_by(name = name).first
        return x
        y = session.query.filter_by(unit_cost= unit_cost).first
        return y
        asset_value = item.total
        total = x*y
        return total 


              

