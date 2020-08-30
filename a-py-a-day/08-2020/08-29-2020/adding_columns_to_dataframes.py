"""
Sometimes, we want to add a column to an existing DataFrame. We might want to add new information or
perform a calculation based on the data that we already have.

One way that we can add a new column is by giving a list of the same length as the existing
DataFrame.
"""

import pandas as pd

df = pd.DataFrame(
    [
        [1, "3 inch screw", 0.5, 0.75],
        [2, "2 inch nail", 0.10, 0.25],
        [3, "hammer", 3.00, 5.50],
        [4, "screwdriver", 2.50, 3.00],
    ],
    columns=["Product ID", "Description", "Cost to Manufacture", "Price"],
)

# Add columns here
df['Sold in Bulk?'] = ["Yes", "Yes", "No", "No"]

print(df)

