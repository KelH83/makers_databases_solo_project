from lib.order import Order

def test_order_constructs():
    order = Order(1,"Kiyomi Barker", '2024-10-14')
    assert order.id == 1
    assert order.customer_name == "Kiyomi Barker"
    assert order.date_placed == '2024-10-14'

def test_order_formats_nicely():
    order = Order(1,"Kiyomi Barker", '2024-10-14')
    assert str(order) == "Order ID:1, Customer Name:Kiyomi Barker, Date Placed:2024-10-14"