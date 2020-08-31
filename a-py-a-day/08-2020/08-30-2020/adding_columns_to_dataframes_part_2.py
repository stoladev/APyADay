"""
Docstring

Modifying DataFrames
Adding a Column II

We can also add a new column that is the same for all rows in the DataFrame


Suppose we know that all of our products are currently in-stock. We can add a column that says this:

df['In Stock?'] = True

Now all of the rows have a column called In Stock? with value True.
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

print(df)

df["Is taxed?"] = "Yes"

