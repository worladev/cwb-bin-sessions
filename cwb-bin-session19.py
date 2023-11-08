'''
SESSION 19 (11/10/2023)
Mentor and Facilitator ==> ANDY AFFUL

TITLE: Grocery Store Program:

PROBLEM STATEMENT: You are tasked with creating a simple Grocery Store class that can manage products and
transactions. Implement the GroceryStore class with the following functionalities:

FUNCTIONALITIES:
- Add Product: Add a new product to the store with a name, price, and quantity.
- Update Product: Update the price and/or quantity of an existing product.
- Remove Product: Remove a product from the store.
- Display Products: Display all products available in the store.
- Make a Purchase: Allow a customer to make a purchase, specifying the product and quantity. Deduct the purchased
    quantity from the product's stock.
- Calculate Total: Calculate and return the total price of the items in the customer's cart.


NOTE: MODIFIED EXAMPLE USAGE DURING IMPLEMENTATION
# Example Usage:
store = GroceryStore()
store.add_product("Apple", 1.0, 50)
store.add_product("Banana", 0.5, 100)
store.display_products()

# Customer makes a purchase
cart = {"Apple": 5, "Banana": 10}
if store.make_purchase(cart):
    total_price = store.calculate_total(cart)
    print("Total Price:", total_price)
else:
    print("Invalid Purchase!")
'''
class GroceryStore:
    def __init__(self):
        self.product = dict() #variable to hold items in the store
        self.cart = dict() #variable to hold selected item to purchase

    # method to add new products to store
    def add_product(self, name, price, quantity):
        self.product[name] = {'price': price, 'quantity':quantity}



# Example Usage:
store = GroceryStore()

#add product to the store
store.add_product("Apple", 1.0, 50)
store.add_product("Banana", 0.5, 100)
store.add_product("Milk", 1.99, 80)
store.add_product("Oat", 1.4, 100)
store.add_product("Orange", 0.7, 150)
store.add_product("Grape", 0.99, 100)

