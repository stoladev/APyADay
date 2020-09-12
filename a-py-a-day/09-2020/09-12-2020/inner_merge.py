"""
Working with Multiple DataFrames
Inner Merge I

Suppose we have the following three tables that describe our eCommerce business

orders — a table with information on each transaction

order_idcustomer_idproduct_idquantitytimestamp
12312017-01-01
22232017-01-01
33112017-01-01
43222017-02-01
53332017-02-01
61422017-03-01
71112017-02-02
81412017-02-02

products — a table with product IDs, descriptions, and prices

product_iddescriptionprice
1thing-a-ma-jig5
2whatcha-ma-call-it10
3doo-hickey7
4gizmo3

customers — a table with customer names and contact information

customer_idcustomer_nameaddressphone_number
1John Smith123 Main St.212-123-4567
2Jane Doe456 Park Ave.949-867-5309
3Joe Schmo798 Broadway112-358-1321

If we just look at the orders table, we can’t really tell what’s happened in each order.
However, if we refer to the other tables, we can get a more complete picture.

Let’s examine the order with an order_id of 1. It was purchased by Customer 2. To find
out the customer’s name, we look at the customers table and look for the item with a
customer_id value of 2. We can see that Customer 2’s name is Jane Doe and that she lives
at 456 Park Ave.

Doing this kind of matching is called merging two DataFrames.
"""

import pandas as pd

orders = pd.read_csv("orders.csv")

products = pd.read_csv("products.csv")

customers = pd.read_csv("customers.csv")

print(orders)
print(products)
print(customers)

order_3_description = "thing-a-ma-jig"
order_5_phone_number = "112-358-1321"

