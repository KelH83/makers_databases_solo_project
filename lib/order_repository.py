from lib.order import Order

class OrderRepository:
    def __init__(self, connection):
        self._connection = connection

    # CREATE

    def create(self, order):
        self._connection.execute('INSERT INTO orders (customer_name, date_placed) VALUES (%s, %s)', [
                                order.customer_name, order.date_placed])
        return None
    
    # READ
    def all(self):
        rows = self._connection.execute('SELECT * from orders')
        orders = []
        for row in rows:
            order = Order(row["id"], row["customer_name"], row["date_placed"])
            orders.append(order)
        return orders
    

    def find(self, order_id):
        rows = self._connection.execute(
            'SELECT * from orders WHERE id = %s', [order_id])
        row = rows[0]
        return Order(row["id"], row["customer_name"], row["date_placed"])
    
    # UPDATE
    def update(self, order_id, new_name):
        self._connection.execute('UPDATE orders SET customer_name = %s WHERE id = %s', [new_name, order_id])
        rows = self._connection.execute('SELECT * FROM orders WHERE id = %s', [order_id])
        row = rows[0]
        return Order(row["id"], row["customer_name"], row["date_placed"])
    
    # DELETE
    def delete(self, order_id):
        self._connection.execute(
            'DELETE FROM orders WHERE id = %s', [order_id])
        return None