from IMA import CategoryModel, ItemModel
from sqlalchemy.orm import Session
session = Session()

class Products:
    def __init__(self, name, details):
        self.name = name
        self.details = details

    
    def get_Item_Category():
      categories= sesssion.query(CategoryModel).all()
      for category in categories:
        print("{} {}".format(category.name, category.details))
        category_id = input('Which Category?')
      return int(category_id)

    def create_category(self, name, details):
        category = CategoryModel(name=name, details=details)
        session.add(category)
        session.commit()
    
    def update_category(self, name, detail):
       categories= session.query(CategoryModel).all()
       print('select which category to update')
       category_id = get_Item_Category
       category = input('enter field to update')
       category_id = session.query.filter_by(category_id= category_id).first
       if not category:
         print('Category not found')
       else:
        new_content = input('Enter new category: ')
        category.category_id = new_content
        session.commit()
        print('Category successfully updated.')

    def delete_category(name, details):
      categories= session.query(CategoryModel).all()
      print('select which category to Delete')
      category_id = get_Item_Category
      category = input('enter field to Delete')
      category_id = session.query.filter_by(category_id= category_id).first
      if not category:
         print('Category not found')
      else:
        category.delete_category
        session.commit()
        print('Category successfully deleted.')

    def view_category(name,details):
        print('select which category to view')
        for instance in session.query(category).order_by(category_id, category_name, category_details):
            print(instance.category_id, instance.name, instance.details)

    def search_category(name,details):
        print('select which category to view')
        for instance in session.query(category).order_by(category_id, category_name, category_details):
            print(instance.category_id, instance.name, instance.details)
    
class Particulars():
    def __init__(self, name, details, unit_cost, total, quantity, status, date_added, category_id):
        self.name = name
        self.details = details
        self.unit_cost = unit_cost
        self.quantity = quantity
        self.date_added = date_added
        self.category_id = category_id

    def get_items_Item():
        items= sesssion.query(CategoryModel).all()
        for item in categories:
            print("{} {}".format(item.name, item.details, item.unit_cost, quantity, item.total, item.date_added, item.status))
            item_id = input('Which item?')
            return int(item_id)

    def create_item(self, name, details, unit_cost, quantity, total, status, date_added):
        item = CategoryModel(name=name, details=details, unit_cost =unit_cost, quantity =quantity, status =status, date_added =date_added)
        session.add(category)
        session.commit()

    def update_item(self, name, details, unit_cost,quantity, total, status, date_added):
       items= session.query(CategoryModel).all()
       print('select which item to update')
       item_id = get_items_Item
       item = input('enter field to update')
       item_id = session.query.filter_by(item_id= item_id).first
       if not item:
         print('item not found')
       else:
        new_content = input('Enter new item: ')
        item.item_id = new_content
        session.commit()
        print('item successfully updated.')

    def delete_item(self, name, details, unit_cost, quantity, total, status, date_added):
        categories= session.query(CategoryModel).all()
        print('select which category to Delete')
        item_id = get_items_Item
        item = input('enter field to Delete')
        item_id = session.query.filter_by(item_id= item_id).first
        if not item:
            print('item not found')
        else:
            item.delete_item
            session.commit()
            print('item successfully deleted.')

    def view_item(name,details, unit_cost,quantity, total,status,date_added):
        print('select which item to view')
        for instance in session.query(item).order_by(item_id, item_name, item_details, item_unit_cost, item_quantity, item_total, item_status):
            print(instance.item_id, instance.name, instance.details, instance.unit_cost, instance.quantity, instance.total, instance.status)

    def search_item(name,details, unit_cost, quantity, total,status,date_added):
        print('select which item to view')
        for instance in session.query(item).order_by(item_id, item_name, item_details, item_unit_cost, item_quantity, item_total, item_status):
            print(instance.item_id, instance.name, instance.details, instance.unit_cost, instance.quantity, instance.total, instance.status)
     
     def assert_value()
      
y = Products("phone", "samsung")
y.create_category("phone", "samsung")      
        