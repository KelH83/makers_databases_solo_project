from lib.item import Item

class ItemRepository:
    def __init__(self, connection):
        self._connection = connection

    # CREATE

    def create(self, item):
        self._connection.execute('INSERT INTO items (name, unit_price, qty) VALUES (%s, %s, %s)', [
                                item.name, item.unit_price, item.qty])
        return None
    
    # READ
    def all(self):
        rows = self._connection.execute('SELECT * from items')
        items = []
        for row in rows:
            item = Item(row["name"], row["unit_price"], row["qty"],row["id"])
            items.append(item)
        return items
    

    def find(self, item_name):
        rows = self._connection.execute(
            'SELECT * from items WHERE name = %s', [item_name])
        row = rows[0]
        return Item(row["name"], row["unit_price"], row["qty"],row["id"])
    
    # UPDATE
    def update(self, item_id, new_name = None, new_qty = None, new_unit_price = None):
        if new_name is not None:
            self._connection.execute('UPDATE items SET name = %s WHERE id = %s', [new_name, item_id])
            rows = self._connection.execute('SELECT * FROM items WHERE id = %s', [item_id])
            row = rows[0]
            return Item(row["id"], row["name"], row["unit_price"], row["qty"])
        elif new_qty is not None:
            self._connection.execute('UPDATE items SET qty = %s WHERE id = %s', [new_qty, item_id])
            rows = self._connection.execute('SELECT * FROM items WHERE id = %s', [item_id])
            row = rows[0]
            return Item(row["id"], row["name"], row["unit_price"], row["qty"])
        else:
            self._connection.execute('UPDATE items SET unit_price = %s WHERE id = %s', [new_unit_price, item_id])
            rows = self._connection.execute('SELECT * FROM items WHERE id = %s', [item_id])
            row = rows[0]
            return Item(row["id"], row["name"], row["unit_price"], row["qty"])
    
    # DELETE
    def delete(self, item_id):
        self._connection.execute(
            'DELETE FROM items WHERE id = %s', [item_id])
        return None