from lib.order_repository import OrderRepository
from lib.order import Order
import datetime


def test_get_all_records(db_connection): 
    db_connection.seed("seeds/shop.sql") 
    repository = OrderRepository(db_connection)

    orders = repository.all() 

    assert orders == [
        Order(1,'Kelly Howes', datetime.date(2024,10,18)),
        Order(2,'Kimiko Dogue', datetime.date(2024,10,12)),
        Order(3,'Twyla Kitty', datetime.date(2024,10,9))
    ]

def test_get_single_record(db_connection):
    db_connection.seed("seeds/shop.sql")
    repository = OrderRepository(db_connection)

    order = repository.find(1)
    assert order == Order(1,'Kelly Howes', datetime.date(2024,10,18))

def test_create_order(db_connection):
    db_connection.seed("seeds/shop.sql")
    repository = OrderRepository(db_connection)

    repository.create(Order(4,"Mini Panther", '2024-10-6'))

    result = repository.all()
    assert result == [
        Order(1,'Kelly Howes', datetime.date(2024,10,18)),
        Order(2,'Kimiko Dogue', datetime.date(2024,10,12)),
        Order(3,'Twyla Kitty', datetime.date(2024,10,9)),
        Order(4,'Mini Panther', datetime.date(2024,10,6))
    ]

def test_update_Order(db_connection):
    db_connection.seed("seeds/shop.sql")
    repository = OrderRepository(db_connection)
    repository.update(1, new_name='Kyoko Howes') 

    order = repository.find(1)
    assert order == Order(1,'Kyoko Howes', datetime.date(2024,10,18))


def test_delete_record(db_connection):
    db_connection.seed("seeds/shop.sql")
    repository = OrderRepository(db_connection)
    repository.delete(3) 

    result = repository.all()
    assert result == [
        Order(1,'Kelly Howes', datetime.date(2024,10,18)),
        Order(2,'Kimiko Dogue', datetime.date(2024,10,12)),
    ]