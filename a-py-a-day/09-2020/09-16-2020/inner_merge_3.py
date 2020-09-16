"""

In addition to using pd.merge, each DataFrame has its own merge method. For instance, if you wanted to merge orders
with customers, you could use:

new_df = orders.merge(customers)

This produces the same DataFrame as if we had called pd.merge(orders, customers).

We generally use this when we are joining more than two DataFrames together because we can “chain” the commands. The
following command would merge orders to customers, and then the resulting DataFrame to products:

big_df = orders.merge(customers)\
    .merge(products)

"""

# We have some more data from Cool T-Shirts Inc. The number of men’s and women’s t-shirts sold per month is in a file
# called men_women_sales.csv. Load this data into a DataFrame called men_women.

import pandas as pd

sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)

men_women = pd.read_csv('men_women_sales.csv')

all_data = sales.merge(targets) \
    .merge(men_women)

results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]
