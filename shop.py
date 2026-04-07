class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name}, {self.price}, {self.stock}"

    def __repr__(self):
        return f"Product name: {self.name}; Price: {self.price}; Stock: {self.stock}"


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
        total = 0
        # `.items()` breaks the dictionary down into pairs
        for item_name, quantity in self.items.items():
            # grab product object, then the price
            price = inventory[item_name].price
            total += price * quantity
        print(f"{total}")

    def checkout(self):
        # update Product's stock
        for item_name, quantity in self.items.items():
            inventory[item_name].stock -= quantity

        # clear self.items
        self.items.clear()


CART = ShoppingCart()

# ---------
# INVENTORY OF PRODUCT OBJECTS
# ---------

inventory = {
    "bread": Product("bread", 2.99, 20),
    "cheese": Product("cheese", 5.25, 10),
    "eggs": Product("eggs", 1.99, 30),
    "milk": Product("milk", 1.29, 20),
    "banana": Product("banana", 0.25, 60),
}

print(inventory)

CART.add_product("bread", 1)
CART.add_product("bread", 1)
CART.add_product("eggs", 1)
CART.add_product("cheese", 2)
CART.add_product("wine", 2)
CART.view_cart()
CART.get_total()
CART.checkout()

print(inventory)
