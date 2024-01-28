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
# importing csv
import csv

# Defining Product class with attributes
class Product:
    def __init__(self, product_id, product_name, quantity, price_per_unit):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price_per_unit = price_per_unit


# Defining Product file reader class with attributes
class ProductFileReader:
    def __init__(self, sales_data_file):
        self.productsList = list()
        self.data_file = sales_data_file
    
    # a file reader method using the DictReader funtion for csv files.
    def read(self):
        with open(self.data_file) as data_file:
            reader = csv.DictReader(data_file)
            for row in reader:
                new_product = Product(
                    row['product_id'],
                    row['product_name'],
                    int(row['quantity']),
                    float(row['price_per_unit'])
                )
                self.productsList.append(new_product)
        return self.productsList


# Defining Data Analysis class to handle computations
class DataAnalysis:
    def __init__(self,):
        self.read_data = ProductFileReader('csvFiles/sales_data.csv')
        self.product_list = self.read_data.read()
        

    # a method to calculate the total sales for each product
    def totol_sales(self):
        for product in self.product_list:
            totalSales = int(product.quantity) * float(product.price_per_unit)
            output = f"Product: {product.product_name}, Total Sales: ${round(totalSales, 2)}"
            print(output)
    
    # a method to print the most expensive product
    def most_expensive(self):
        mostExpensive = ""
        price = 0.0
        for product in self.product_list:
            if float(product.price_per_unit) > float(price):
                price = product.price_per_unit
                mostExpensive = product.product_name
            else:
                continue
        print(f"Most Expensive Product: {mostExpensive}")


# creating an instance of the DataAnalysis class
analyse_data = DataAnalysis()
analyse_data.totol_sales()
      

