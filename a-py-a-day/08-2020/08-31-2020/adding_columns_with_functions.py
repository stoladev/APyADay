"""
Finally, you can add a new column by performing a function on the existing columns.

Maybe we want to add a column to our inventory table with the amount of sales tax that we need to
charge for each item.
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

df["Margin"] = df.Price - df["Cost to Manufacture"]

print(df)

