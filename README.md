# python_shopping_cart

This is an optional mini-project for the Data Analysis pathway for Code:You.

##Project Overview
You’ll be simulating the backend of a basic online store. The system will let users browse products, add them to a shopping cart, and complete a checkout process.

## Core Components
### Product
- Attributes: name, price, stock
- Represents an individual item in the store
### Store
- Holds a list of Product objects
- Displays the current inventory
- Includes a method to look up a product by name
### ShoppingCart
- Stores items and quantities selected by the user
- Includes methods to:
  - Add a product
  - Remove a product
  - View cart contents
  - Get total cost
  - Checkout (update stock, clear cart)
### Basic Requirements
- [ ] The store should start with at least five products
- [ ] The user should be able to add and remove products from the cart, but not exceed available stock
- [ ] The user should be able to view their cart and see a total price
When checking out, the system should update the stock levels and clear the cart
### Stretch Goals (Optional)
Try adding any of the following if you want to go further:
- [ ] Apply tax or discounts at checkout
- [ ] Store purchase history
- [ ] Gracefully handle out-of-stock items
- [ ] Add a Customer class and support multiple users
- [ ] Load or save product data from a CSV file
- [ ] Think ahead: how could you turn this into a GUI or web app?
### Reflection Questions
Once you've tried building it, take a moment to reflect:

- What does this remind you of from real life?
- Which parts of your code could be reused in another program?
- What are some next steps you could take to build this out further?

#### AI Disclaimer
After much searching online I did use Chat GPT to help in figuring out:
- How to implement the `__str__` functionality
- Checking the inventory as a dictionary
- The get total loop when working with the inventory dictionary and the `items()` method