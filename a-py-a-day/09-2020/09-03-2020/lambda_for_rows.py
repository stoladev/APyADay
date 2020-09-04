"""
We can also operate on multiple columns at once. If we use apply without specifying a single column
and add the argument axis=1, the input to our lambda function will be an entire row, not a column.
To access particular values of the row, we use the syntax row.column_name or row[‘column_name’].

Suppose we have a table representing a grocery list:
Item    Price   Is taxed?
Apple   1.00    No
Milk    4.20    No
Paper Towels    5.00    Yes
Light Bulbs     3.75    Yes

If we want to add in the price with tax for each line, we’ll need to look at two columns: Price and
Is taxed?.

If Is taxed? is Yes, then we’ll want to multiply Price by 1.075 (for 7.5% sales tax).

If Is taxed? is No, we’ll just have Price without multiplying it.

We can create this column using a lambda function and the keyword axis=1:

df['Price with Tax'] = df.apply(lambda row:
    row['Price'] * 1.075
    if row['Is taxed?'] == 'Yes'
    else row['Price'],
    axis=1
)
"""

# If an employee worked for more than 40 hours, she needs to be paid overtime (1.5 times the normal
# hourly wage).

# For instance, if an employee worked for 43 hours and made $10/hour, she would receive $400 for the
# first 40 hours that she worked, and an additional $45 for the 3 hours of overtime, for a total for
# $445.

# Create a lambda function total_earned that accepts an input row with keys hours_worked and
# hourly_wage and uses an if statement to calculate the hourly wage.

import pandas as pd

df = pd.read_csv("employees.csv")

total_earned = (
    lambda row: (row.hourly_wage * 40)
    + ((row.hourly_wage * 1.5) * (row.hours_worked - 40))
    if row.hours_worked > 40
    else row.hourly_wage * row.hours_worked
)

df["total_earned"] = df.apply(total_earned, axis=1)

print(df)

