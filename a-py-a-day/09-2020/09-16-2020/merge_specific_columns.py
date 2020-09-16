"""

In the previous example, the merge function “knew” how to combine tables based on the columns that were the same
between two tables. For instance, products and orders both had a column called product_id. This won’t always be true
when we want to perform a merge.

Generally, the products and customers DataFrames would not have the columns product_id or customer_id. Instead, they
would both be called id and it would be implied that the id was the product_id for the products table and customer_id
for the customers table. They would look like this:

Customers
id	customer_name	address	phone_number
1	John Smith	123 Main St.	212-123-4567
2	Jane Doe	456 Park Ave.	949-867-5309
3	Joe Schmo	798 Broadway	112-358-1321

Products
id	description	price
1	thing-a-ma-jig	5
2	whatcha-ma-call-it	10
3	doo-hickey	7
4	gizmo	3

**How would this affect our merges?**

Because the id columns would mean something different in each table, our default merges would be wrong.

One way that we could address this problem is to use .rename to rename the columns for our merges. In the example
below, we will rename the column id to customer_id, so that orders and customers have a common column for the merge.

pd.merge(
    orders,
    customers.rename(columns={'id': 'customer_id'}))

"""

# Merge orders and products using rename. Save your results to the variable orders_products.

import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)

orders_products = pd.merge(orders, products.rename(columns={'id': 'product_id'}))

"""

We could use the keywords left_on and right_on to specify which columns we want to perform the merge on. In the example
below, the “left” table is the one that comes first (orders), and the “right” table is the one that comes second
(customers). This syntax says that we should match the customer_id from orders to the id in customers.

pd.merge(
    orders,
    customers,
    left_on='customer_id',
    right_on='id')

If we use this syntax, we’ll end up with two columns called id, one from the first table and one from the second. 
Pandas won’t let you have two columns with the same name, so it will change them to id_x and id_y.

It will look like this:
id_x 	customer_id 	product_id 	quantity 	timestamp 	id_y 	customer_name 	address 	phone_number
1 	2 	3 	1 	2017-01-01 00:00:00 	2 	Jane Doe 	456 Park Ave 	949-867-5309
2 	2 	2 	3 	2017-01-01 00:00:00 	2 	Jane Doe 	456 Park Ave 	949-867-5309
3 	3 	1 	1 	2017-01-01 00:00:00 	3 	Joe Schmo 	789 Broadway 	112-358-1321
4 	3 	2 	2 	2016-02-01 00:00:00 	3 	Joe Schmo 	789 Broadway 	112-358-1321
5 	3 	3 	3 	2017-02-01 00:00:00 	3 	Joe Schmo 	789 Broadway 	112-358-1321
6 	1 	4 	2 	2017-03-01 00:00:00 	1 	John Smith 	123 Main St. 	212-123-4567
7 	1 	1 	1 	2017-02-02 00:00:00 	1 	John Smith 	123 Main St. 	212-123-4567
8 	1 	4 	1 	2017-02-02 00:00:00 	1 	John Smith 	123 Main St. 	212-123-4567

The new column names id_x and id_y aren’t very helpful for us when we read the table. We can help make them more useful
by using the keyword suffixes. We can provide a list of suffixes to use instead of “_x” and “_y”.

For example, we could use the following code to make the suffixes reflect the table names:

pd.merge(
    orders,
    customers,
    left_on='customer_id',
    right_on='id',
    suffixes=['_order', '_customer']
)

The resulting table would look like this:
id_order 	customer_id 	product_id 	quantity 	timestamp 	id_customer 	customer_name 	address 	phone_number
1 	2 	3 	1 	2017-01-01 00:00:00 	2 	Jane Doe 	456 Park Ave 	949-867-5309
2 	2 	2 	3 	2017-01-01 00:00:00 	2 	Jane Doe 	456 Park Ave 	949-867-5309
3 	3 	1 	1 	2017-01-01 00:00:00 	3 	Joe Schmo 	789 Broadway 	112-358-1321
4 	3 	2 	2 	2016-02-01 00:00:00 	3 	Joe Schmo 	789 Broadway 	112-358-1321
5 	3 	3 	3 	2017-02-01 00:00:00 	3 	Joe Schmo 	789 Broadway 	112-358-1321
6 	1 	4 	2 	2017-03-01 00:00:00 	1 	John Smith 	123 Main St. 	212-123-4567
7 	1 	1 	1 	2017-02-02 00:00:00 	1 	John Smith 	123 Main St. 	212-123-4567
8 	1 	4 	1 	2017-02-02 00:00:00 	1 	John Smith 	123 Main St. 	212-123-4567

"""

# Merge orders and products using left_on and right_on. Use the suffixes _orders and _products. Save your results to
# the variable orders_products.

orders_products = pd.merge(orders, products, left_on='product_id',
                           right_on='id',
                           suffixes=['_orders', '_products'])

# We’ve just released a new product with product_id equal to 5. People are ordering this product, but we haven’t
# updated the products table.
# In script.py, you’ll find two DataFrames: products and orders. Inspect these DataFrames using print.
# Notice that the third order in orders is for the mysterious new product, but that there is no product_id 5 in
# products.

orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')

print(orders)

# Merge orders and products and save it to the variable merged_df.
# Inspect merged_df using:
# print(merged_df)
# What happened to order_id 3?

merged_df = pd.merge(orders, products)
