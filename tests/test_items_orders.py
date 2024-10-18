from lib.items_orders import ItemsOrders

def test_items_orders_constructs():
    items_orders = ItemsOrders(2,2)
    assert items_orders.item_id == 2
    assert items_orders.order_id == 2

def test_items_items_orderss_formats_nicely():
    items_orders = ItemsOrders(2,2)
    assert str(items_orders) == "Item ID:2, Order ID:2"