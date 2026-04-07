class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


class ShoppingCart:
    def __init__(self):
        self.items = {}  # {product: quantity}

    def add_product(self, product, quantity):
        # push product and quantity to self.items
        if product.name in self.items:
            self.items[product.name] += quantity
        else:
            self.items[product.name] = quantity
        print(f"{quantity} {product.name} product(s) added to the cart.")

    def remove_product(self, product, quantity):
        # remove product(s) from self.items
        if product.name in self.items:
            self.items[product.name] -= quantity
            print(f"{quantity} {product.name} product(s) removed from the cart.")
        else:
            print(f"{product.name} is not in your cart.")

    def view_cart(self):
        # view self.items
        print(f"{self.items}")

    def get_total(self):
        pass
        # sum prices of all self.items
        # Reference the Product's object for price

    def checkout(self):
        pass
        # update Product's stock
        # clear self.items


CART = ShoppingCart()

# ---------
# INVENTORY
# ---------

bread = Product("bread", 2.99, 20)
cheese = Product("cheese", 5.25, 10)
eggs = Product("eggs", 1.99, 30)
milk = Product("milk", 1.29, 20)
banana = Product("banana", 0.25, 60)

CART.add_product(bread, 1)
CART.add_product(bread, 1)
CART.add_product(eggs, 1)
CART.add_product(cheese, 2)
CART.view_cart()
CART.remove_product(bread, 1)
CART.view_cart()
