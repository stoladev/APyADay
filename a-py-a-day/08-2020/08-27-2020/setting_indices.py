"""

When we select a subset of a DataFrame using logic, we end up with non-consecutive indices. This is
inelegant and makes it hard to use .iloc().

We can fix this using the method .reset_index().

If we use the command df.reset_index(), we get a new DataFrame with a new set of indices.

Note that the old indices have been moved into a new column called 'index'. Unless you need those
values for something special, it’s probably better to use the keyword drop=True so that you don’t
end up with that extra column.

Using .reset_index() will return a new DataFrame, but we usually just want to modify our existing
DataFrame. If we use the keyword inplace=True we can just modify our existing DataFrame.

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

df2 = df.loc[[1, 3, 5]]

# df3 = df2.reset_index()
df3 = df2.reset_index(inplace=True, drop=True)

