"""
Welcome to Inventory Management Application.
Usage:
	 create_category <category_id> <name> <details>
	 update_category <category_name> 
	 delete_category <category_id> 
	 view_category <category_id> <name> <details>
	 search_category <category_id> <name> <details>

	 create_item <item_id> <name> <details> <quantity> <unit_cost> <total> <status> <date_added> <category_id>
	 update_item <item_id>
	 delete_item <item_id>
	 view_item <item_id> <name> <details> <quantity> <unit_cost> <total> <status> <date_added> <category_id>
	 search_item <item_id> <name> <details> <quantity> <unit_cost> <total> <status> <date_added> <category_id>
	 asset_value <quantity> <unit_cost>
	
Options:
	-i, --interactive  Interactive Mode
	-h, --help  Show this screen and exit.
"""
import cmd
import os
import sys
from docopt import  docopt, DocoptExit
from pyfiglet import Figlet
from IMA import CategoryModel, ItemModel
from inventory import Products, Particulars
from termcolor import colored, cprint
from colorama import init, Fore, Back

product = Products()
particular = Particulars()


init()
font = Figlet(font='epic')
introduction = font.renderText('I.M.A')
os.system('cls')
cprint(introduction, "magenta", attrs=['blink'])

def docopt_cmd(func):
	
	def fn(self, arg):
		try:
			opt = docopt(fn.__doc__, arg)

		except DocoptExit as e:
			# The DocoptExit is thrown when the args do not match.
			# We print a message to the user and the usage block.

			print('Invalid Command!')
			print(e)
			return

		except SystemExit:
			# The SystemExit exception prints the usage for --help
			# We do not need to do the print here.

			return

		return func(self, opt)

	fn.__name__ = func.__name__
	fn.__doc__ = func.__doc__
	fn.__dict__.update(func.__dict__)
	return fn

class Display(cmd.Cmd):
	cprint("* * * * * * * * * * * * * * * * * * * * * * * * *",'cyan', attrs=['bold'])
	cprint("*                                               *",'cyan', attrs=['bold'])
	cprint("*  INVENTORY MANAGEMENT APPLICATION             *",'cyan', attrs=['bold'])
	cprint("*                                               *",'cyan', attrs=['bold'])
	cprint("* * * * * * * * * * * * * * * * * * * * * * * * *",'cyan', attrs=['bold'])
	cprint("*   SELECT TO EXECUTE:                          *",'cyan', attrs=['bold'])
	cprint("*************************************************",'cyan', attrs=['bold'])
	cprint("*A.category.                                    *",'cyan', attrs=['bold'])
	cprint("*************************************************",'cyan', attrs=['bold'])
	cprint("*1.CREATE CATEGORY.                             *",'cyan', attrs=['bold'])
	cprint("*2.UPDATE CATEGORY.                             *",'cyan', attrs=['bold'])
	cprint("*3.DELETE CATEGORY.                             *",'cyan', attrs=['bold'])
	cprint("*4.VIEW CATEGORY.                               *",'cyan', attrs=['bold'])
	cprint("*5.SEARCH CATEGORY.                             *",'cyan', attrs=['bold'])
	cprint("*************************************************",'cyan', attrs=['bold'])
	cprint("*B.items.                                       *",'cyan', attrs=['bold'])
	cprint("*************************************************",'cyan', attrs=['bold'])
	cprint("*1.CREATE ITEM.                                 *",'cyan', attrs=['bold'])
	cprint("*2.UPDATE ITEM.                                 *",'cyan', attrs=['bold'])
	cprint("*3.DELETE ITEM.                                 *",'cyan', attrs=['bold'])
	cprint("*4.VIEW   ITEM.                                 *",'cyan', attrs=['bold'])
	cprint("*5.SEARCH ITEM.                                 *",'cyan', attrs=['bold'])
	cprint("*************************************************",'cyan', attrs=['bold'])

	prompt = "<Enter> "

class Inventory(cmd.Cmd):

	@docopt_cmd
	def do_create_category(self, args):
		"""Usage: category_add <name> <details> <quantity>"""
		name = args['<name>']
		details = args['<details>']
		
		product.create_category(name, details)

	@docopt_cmd
	def do_update_category(self,args):
		"""Usage: update_category <category_name>"""
		name = args['<name>']
		product.update_category(name)

	@docopt_cmd
	def do_delete_category(self,args):
		"""Usage: delete_category <category_id>"""
		name = args['<name>']
		product.delete_category

	@docopt_cmd
	def do_view_categery(self,args):
		"""Usage: view_category <category_id>"""
		name = args['<name>']
		product.view_category

	@docopt_cmd
	def search_view_category(self,args):
		"""Usage: search_category <category_id>"""
		name = args['<name>']
		product.search_category

	@docopt_cmd
	def do_create_item(self, args):
		"""Usage: item_add <name> <details> <quantity> <unit_cost> <total> <status> <date_added> <category_id>"""
		name = args['<name>']
		description = args['<details>']
		quantity = args['<quantity>']
		unit_cost = args['<unit_']
		total = args['<total>']
		status = args['<status>']
		date_added = args['<date>']
		category_id = args['<category_id>']
		Particulars.create_item

	@docopt_cmd
	def do_update_item(self, args):
		"""Usage: update_item <item_name>"""
		name = args['<name>']
		Particulars.update_category

	@docopt_cmd
	def do_delete_item(self, args):
		"""Usage: delete_item <item_name>"""
		name = args['<name>']
		Particulars.delete_category	
	
	@docopt_cmd
	def do_delete_item(self, args):
		"""Usage: search_item <item_name>"""
		name = args['<name>']
		Particulars.search_category	

	def do_quit(self, arg):
		"""Quits out of Interactive Mode."""
		
		cprint('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *','cyan', attrs=['bold'])
		cprint('*                                                           *','cyan', attrs=['bold'])
		cprint('*       BYE! YOU HAVE SUCCESSFULLY EXITED THE PROGRAM       *','cyan', attrs=['bold'])
		cprint('*                                                           *','cyan', attrs=['bold'])
		cprint('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *','cyan', attrs=['bold'])
		exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
	Display().cmdloop()

print(opt)
	




 
