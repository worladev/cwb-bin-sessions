'''
SESSION 23 (30/10/2023)
Mentor and Facilitator ==> ANDY AFFUL

TITLE: Analyzing Sales Data

PROBLEM STATEMENT: You are given a file named "sales_data.txt" containing sales data of a store. Each line of
the file represents the sales of a specific product and has the following format: ProductID, ProductName,
Quantity,PricePerUnit. Here's an example of the contents of "sales_data.txt":

-----------------------
101,Widget A,50,10.5
102,Widget B,30,8.2
103,Widget C,20,12.0
104,Widget D,40,9.5
-----------------------
Write a Python program to read the data from "sales_data.txt" and perform the following tasks:

== Total Sales:
Calculate and print the total sales (Quantity multiplied by PricePerUnit) for each product.
Format the output like this:
Product: Widget A, Total Sales: $525.0
Product: Widget B, Total Sales: $246.0

== Most Expensive Product:
Determine and print the product with the highest price per unit.

== Average Quantity:
Calculate and print the average quantity sold across all products.

== Products Below Average:
Identify and print the products with quantities sold below the average quantity.

CONSTRAINTS: All numerical values in the file are non-negative integers or positive floating-point numbers.

Example Output:
Product: Widget A, Total Sales: $525.0
Product: Widget B, Total Sales: $246.0
Product: Widget C, Total Sales: $240.0
Product: Widget D, Total Sales: $380.0

Most Expensive Product: Widget C

Average Quantity: 35.0

Products Below Average Quantity:
Product: Widget B, Quantity: 30
Product: Widget C, Quantity: 20
'''
# Defining Product class
class Product:
    def __init__(self, product_id, product_name, quantity, price_per_unit):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

