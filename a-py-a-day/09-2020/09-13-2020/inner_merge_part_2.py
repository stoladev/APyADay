"""
It is easy to do this kind of matching for one row, but hard to do it for multiple rows.

Luckily, Pandas can efficiently do this for the entire table. We use the .merge method.

The .merge method looks for columns that are common between two DataFrames and then looks for rows
where those column’s values are the same. It then combines the matching rows into a single row in a
new table.

We can call the pd.merge method with two tables like this

new_df = pd.merge(orders, customers)

This will match up all of the customer information to the orders that each customer made.

"""

import pandas as pd

sales = pd.read_csv("sales.csv")
print(sales)
targets = pd.read_csv("targets.csv")
print(targets)

sales_vs_targets = pd.merge(sales, targets)

print(sales_vs_targets)

crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]

