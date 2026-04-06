class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


class ShoppingCart:
    def __init__(self):
        self.items = {}  # {product: quantity}

    def add_product(self, product, quantity):
        pass
        # push product and quantity to self.items

    def remove_product(self, product, quantity):
        pass
        # pop/remove product(s) from self.items

    def view_cart(self):
        pass
        # view self.items

    def get_total(self):
        pass
        # sum prices of all self.items
        # Reference the Product's object for price

    def checkout(self):
        pass
        # update Product's stock
        # clear self.items
