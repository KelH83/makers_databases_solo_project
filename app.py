from lib.database_connection import DatabaseConnection
from lib.item_repository import ItemRepository
from lib.item import Item
from lib.order_repository import OrderRepository
from lib.order import Order
from lib.items_orders_repository import ItemsOrdersRepository
from lib.items_orders import ItemsOrders

connection = DatabaseConnection()
connection.connect()

connection.seed("seeds/shop.sql")


print('Welcome to the shop management program!\n')
selection = input('What do you want to do?\n\n 1 = list all shop items\n 2 = create new shop item\n 3 = list all orders\n 4 = create a new order\n 5 = update an item\n 6 = update an order\n 7 = View items in an order\n 8 = Add items to order\n\n Selection:')

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

elif selection == '3':
    print("Here's a list of all orders:\n")
    order_repository = OrderRepository(connection)
    orders = order_repository.all()
    for order in orders:
        print(order)

elif selection == '4':
    customer_name = input("What is the customer's name? ")
    date_placed = input("What is the order date?")
    order_repository = OrderRepository(connection)
    order_repository.create(Order(customer_name,date_placed))
    print(f"Order successfully added")
    orders = order_repository.all()
    for order in orders:
        print(order)

elif selection == '5':
    item_id = input('What is the ID of the item you wish to update?')
    update_option = input('What do you want to update?\n 1 = name\n 2 = qty\n 3 = price ')
    if update_option == '1':
        new_name = input('What is the new name? ')
        item_repository = ItemRepository(connection)
        item_repository.update(item_id, new_name)
        print('Item successfully updated')
        print(item_repository.find(new_name))
    elif update_option == '2':
        name = input('What is the item name? ')
        new_qty = input('What is the new qty? ')
        item_repository = ItemRepository(connection)
        item_repository.update(item_id, None, new_qty)
        print('Item successfully updated')
        print(item_repository.find(name))
    elif update_option == '3':
        name = input('What is the item name? ')
        new_unit_price = input('What is the new unit price? ')
        item_repository = ItemRepository(connection)
        item_repository.update(item_id, None, None, new_unit_price)
        print('Item successfully updated')
        print(item_repository.find(name))

elif selection == '6':
    order_id = input('What is the ID of the order you wish to update? ')
    new_name = input('What is the amended customer name? ')
    order_repository = OrderRepository(connection)
    order_repository.update(order_id, new_name)
    print('Order successfully updated')
    print(order_repository.find(order_id))

elif selection == '7':
    order_id = input('What is the ID of the order you wish to view the items of? ')
    items_orders_repository = ItemsOrdersRepository(connection)
    items = items_orders_repository.get_order_items(order_id)
    for item in items:
        print(item)

else:
    item_id = input('What is the item ID? ')
    order_id = input('What is the order ID? ')
    items_orders_repository = ItemsOrdersRepository(connection)
    items_orders_repository.create(ItemsOrders(item_id, order_id))
    items = items_orders_repository.get_order_items(order_id)
    for item in items:
        print(item)
