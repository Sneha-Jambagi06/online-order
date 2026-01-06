class Order:
    def __init__(self, order_id, product, quantity, price):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.price = price

    def total_price(self):
        return self.quantity * self.price

    def process_order(self):
        if self.quantity <= 0:
            return "Invalid Order"
        return "Order Processed"
