from lib.item_repository import ItemRepository
from lib.item import Item


def test_get_all_records(db_connection): 
    db_connection.seed("seeds/shop.sql") 
    repository = ItemRepository(db_connection)

    items = repository.all() 

    assert items == [
        Item(1,'Apples', 0.42, 40),
        Item(2,'Broccoli', 0.82, 20),
        Item(3,'Chicken', 5.00, 10),
        Item(4,'Dijon Mustard', 0.59, 15),
        Item(5,'Pasta', 1.29, 20),
        Item(6,'Baked beans', 0.42, 30),
        Item(7,'Chocolate bar', 0.49, 25),
        Item(8,'Toilet roll', 1.45, 10)
    ]

def test_get_single_record(db_connection):
    db_connection.seed("seeds/shop.sql")
    repository = ItemRepository(db_connection)

    item = repository.find("Chicken")
    assert item == Item(3,'Chicken', 5.00, 10)

def test_create_record(db_connection):
    db_connection.seed("seeds/shop.sql")
    repository = ItemRepository(db_connection)

    repository.create(Item(9,"Pears", 0.49, 20))

    result = repository.all()
    assert result == [
        Item(1,'Apples', 0.42, 40),
        Item(2,'Broccoli', 0.82, 20),
        Item(3,'Chicken', 5.00, 10),
        Item(4,'Dijon Mustard', 0.59, 15),
        Item(5,'Pasta', 1.29, 20),
        Item(6,'Baked beans', 0.42, 30),
        Item(7,'Chocolate bar', 0.49, 25),
        Item(8,'Toilet roll', 1.45, 10),
        Item(9,"Pears", 0.49, 20)
    ]

def test_update_item(db_connection):
    db_connection.seed("seeds/shop.sql")
    repository = ItemRepository(db_connection)
    repository.update(2, new_name='Cauliflower') 
    repository.update(2, new_qty=25) 

    item = repository.find("Cauliflower")
    assert item == Item(2,'Cauliflower', 0.82, 25)


def test_delete_record(db_connection):
    db_connection.seed("seeds/shop.sql")
    repository = ItemRepository(db_connection)
    repository.delete(4) 

    result = repository.all()
    assert result == [
        Item(1,'Apples', 0.42, 40),
        Item(2,'Broccoli', 0.82, 20),
        Item(3,'Chicken', 5.00, 10),
        Item(5,'Pasta', 1.29, 20),
        Item(6,'Baked beans', 0.42, 30),
        Item(7,'Chocolate bar', 0.49, 25),
        Item(8,'Toilet roll', 1.45, 10),
    ]