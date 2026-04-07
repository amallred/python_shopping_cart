class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name}, {self.price}, {self.stock}"


class ShoppingCart:
    def __init__(self):
        self.items = {}  # {product: quantity}

    def add_product(self, product, quantity):
        # push product and quantity to self.items
        if product in inventory:
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
            print(f"{quantity} {product} product(s) added to the cart.")
        else:
            print(f"{product} is not in the store's inventory")

    def remove_product(self, product, quantity):
        # remove product(s) from self.items
        if product in self.items:
            self.items[product] -= quantity
            print(f"{quantity} {product} product(s) removed from the cart.")
        else:
            print(f"{product} is not in your cart.")

    def view_cart(self):
        # view self.items
        print(f"{self.items}")

    def get_total(self):
        # sum prices of all self.items
        # Reference the Product's object for price
        total = 0
        print(self.items)
        for item in self.items:
            # price = item[1]
            # total += price
            print(item)
        print(f"{total}")

    def checkout(self):
        pass
        # update Product's stock
        # clear self.items


CART = ShoppingCart()

# ---------
# INVENTORY OBJECTS
# ---------

# Make this a dictionary

inventory = {
    "bread": Product("bread", 2.99, 20),
    "cheese": Product("cheese", 5.25, 10),
    "eggs": Product("eggs", 1.99, 30),
    "milk": Product("milk", 1.29, 20),
    "banana": Product("banana", 0.25, 60),
}

# bread = Product("bread", 2.99, 20)
# cheese = Product("cheese", 5.25, 10)
# eggs = Product("eggs", 1.99, 30)
# milk = Product("milk", 1.29, 20)
# banana = Product("banana", 0.25, 60)

print(inventory.values())

CART.add_product("bread", 1)
# CART.add_product(bread, 1)
# CART.add_product(eggs, 1)
# CART.add_product(cheese, 2)
CART.view_cart()
# CART.get_total()
# print(bread.price)
