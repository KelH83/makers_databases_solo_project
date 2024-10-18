from lib.items_orders_repository import ItemsOrdersRepository
from lib.items_orders import ItemsOrders


def test_get_all_records(db_connection): 
    db_connection.seed("seeds/shop.sql") 
    repository = ItemsOrdersRepository(db_connection)

    items_orders = repository.all() 

    assert items_orders == [
        ItemsOrders(1, 1),
        ItemsOrders(1, 2),
        ItemsOrders(1, 3),
        ItemsOrders(2, 1),
        ItemsOrders(2, 3),
        ItemsOrders(3, 1),
        ItemsOrders(3, 2),
        ItemsOrders(3, 3),
        ItemsOrders(4, 3),
        ItemsOrders(5, 1),
        ItemsOrders(5, 2),
        ItemsOrders(6, 1),
        ItemsOrders(6, 2),
        ItemsOrders(7, 1),
        ItemsOrders(7, 3),
        ItemsOrders(8, 1),
        ItemsOrders(8, 2),
    ]

def test_create_items_orders(db_connection):
    db_connection.seed("seeds/shop.sql")
    repository = ItemsOrdersRepository(db_connection)

    repository.create(ItemsOrders(2,2))

    result = repository.all()
    assert result == [
        ItemsOrders(1, 1),
        ItemsOrders(1, 2),
        ItemsOrders(1, 3),
        ItemsOrders(2, 1),
        ItemsOrders(2, 3),
        ItemsOrders(3, 1),
        ItemsOrders(3, 2),
        ItemsOrders(3, 3),
        ItemsOrders(4, 3),
        ItemsOrders(5, 1),
        ItemsOrders(5, 2),
        ItemsOrders(6, 1),
        ItemsOrders(6, 2),
        ItemsOrders(7, 1),
        ItemsOrders(7, 3),
        ItemsOrders(8, 1),
        ItemsOrders(8, 2),
        ItemsOrders(2, 2),
    ]

def test_returns_all_order_items(db_connection):
    db_connection.seed("seeds/shop.sql") 
    repository = ItemsOrdersRepository(db_connection)

    all_items = repository.get_order_items(1) 

    assert all_items ==[
        'Apples',
        'Broccoli',
        'Chicken',
        'Pasta',
        'Baked beans',
        'Chocolate bar',
        'Toilet roll'
    ]