class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.quantity * self.price

    def update_price(self, percentage):
        self.price = self.price * (1 + percentage / 100)

    def __str__(self):
        return f"{self.name}, ${self.price:.2f}, {self.quantity}"



p1 = Product("Laptop", 1000, 5)
p2 = Product("Headphones", 200.0, 2)

print(p1)
print(p2)

total1 = p1.total()
total2 = p2.total()

Product.update_price(p1, 20)
print(p1.price)