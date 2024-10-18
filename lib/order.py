class Order:
    def __init__(self, id, customer_name, date_placed):
        self.id = id
        self.customer_name = customer_name
        self.date_placed = date_placed

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Order ID:{self.id}, Customer Name:{self.customer_name}, Date Placed:{self.date_placed}"
