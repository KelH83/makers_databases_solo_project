from lib.database_connection import DatabaseConnection
from lib.item_repository import ItemRepository
from lib.item import Item
from lib.order_repository import OrderRepository
from lib.order import Order

connection = DatabaseConnection()
connection.connect()

connection.seed("seeds/shop.sql")


print('Welcome to the shop management program!\n')
selection = input('What do you want to do?\n\n 1 = list all shop items\n 2 = create new shop item\n 3 = list all orders\n 4 = create a new order\n 5 = update an item\n 6 = update an order\n 7 = View items in an order\n\n Selection:')

if selection == '1':
    print("Here's a list of all shop items:\n")
    item_repository = ItemRepository(connection)
    items = item_repository.all()
    for item in items:
        print(item)

elif selection == '2':
    name = input("What is the item name? ")
    unit_price = float(input("what is the items unit price? "))
    qty = int(input("How many do you want to add? "))
    item_repository = ItemRepository(connection)
    item_repository.create(Item(name,unit_price,qty))
    print(f"Item {name} successfully added")
    items = item_repository.all()
    for item in items:
        print(item)