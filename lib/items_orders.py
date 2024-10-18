class ItemsOrders:
    def __init__(self, item_id, order_id):
        self.item_id = item_id
        self.order_id = order_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Item ID:{self.item_id}, Order ID:{self.order_id}"
