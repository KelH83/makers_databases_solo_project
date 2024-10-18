class Item:
    def __init__(self, name, unit_price, qty, id=None, ):
        self.id = id
        self.name = name
        self.unit_price = unit_price
        self.qty = qty

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Item ID:{self.id}, Name:{self.name}, Unit Price:{self.unit_price}, Qty:{self.qty}"
