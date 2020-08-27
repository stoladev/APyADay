"""
When you have a larger DataFrame, you might want to select just a few columns.

To select two or more columns from a DataFrame, we use a list of the column names. To create the
DataFrame shown above, we would use:

new_df = orders[['last_name', 'email']]

*Note: *Make sure that you have a double set of brackets ([[]]), or this command won’t work!
"""

import pandas as pd

df = pd.DataFrame(
    [
        ["January", 100, 100, 23, 100],
        ["February", 51, 45, 145, 45],
        ["March", 81, 96, 65, 96],
        ["April", 80, 80, 54, 180],
        ["May", 51, 54, 54, 154],
        ["June", 112, 109, 79, 129],
    ],
    columns=["month", "clinic_east", "clinic_north", "clinic_south", "clinic_west"],
)

clinic_north_south = df[["clinic_north", "clinic_south"]]

print(type(clinic_north_south))

"""
Maybe our Customer Service department has just received a message from Joyce Waller, so we want to
know exactly what she ordered. We want to select this single row of data.

DataFrames are zero-indexed, meaning that we start with the 0th row and count up from there. Joyce
Waller’s order is the 2nd row.

We select it using the following command:

orders.iloc[2]

When we select a single row, the result is a Series (just like when we select a single column).
"""

march = df.iloc[2]

"""
You can also select multiple rows from a DataFrame.

Here are some different ways of selecting multiple rows:

orders.iloc[3:7]

would select all rows starting at the 3rd row and up to but not including the 7th row (i.e., the
3rd row, 4th row, 5th row, and 6th row)

orders.iloc[:4]

would select all rows up to, but not including the 4th row (i.e., the 0th, 1st, 2nd, and 3rd rows)

orders.iloc[-3:]
would select the rows starting at the 3rd to last row and up to and including the final row
"""

april_may_june = df.iloc[3:6]

print(april_may_june)
