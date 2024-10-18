from lib.items_orders import ItemsOrders

class ItemsOrdersRepository:
    def __init__(self, connection):
        self._connection = connection

    # CREATE

    def create(self, items_orders):
        self._connection.execute('INSERT INTO items_orders (item_id, order_id) VALUES (%s, %s)', [
                                items_orders.item_id, items_orders.order_id])
        return None
    
    # READ
    def all(self):
        rows = self._connection.execute('SELECT * from items_orders')
        items_orders = []
        for row in rows:
            order = ItemsOrders(row["item_id"], row["order_id"])
            items_orders.append(order)
        return items_orders
    
    #Return all items for a single order

    def get_order_items(self, order_id):
            rows = self._connection.execute('SELECT items.name FROM items_orders JOIN orders ON items_orders.order_id = orders.id JOIN items ON items_orders.item_id = items.id WHERE orders.id = %s',[order_id])
            items = []
            for row in rows:
                items.append(row["name"])
            return items