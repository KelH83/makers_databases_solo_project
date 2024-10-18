from lib.item import Item

def test_item_constructs():
    item = Item("Pears", 0.49, 20)
    assert item.name == "Pears"
    assert item.unit_price == 0.49
    assert item.qty == 20

def test_items_format_nicely():
    item = Item("Pears", 0.49, 20)
    assert str(item) == "Name:Pears, Unit Price:0.49, Qty:20"