"""
In the previous exercise, we learned how to add columns to a DataFrame.

Often, the column that we want to add is related to existing columns, but requires a calculation
more complex than multiplication or addition.

For example, imagine that we have the following table of customers.

It’s a little annoying that the capitalization is different for each row. Perhaps we’d like to make
it more consistent by making all of the letters uppercase.

We can use the apply function to apply a function to every value in a particular column. For
example, this code overwrites the existing 'Name' columns by applying the function upper to every
row in 'Name'.

    from string import upper

    df['Name'] = df.Name.apply(upper)

"""


# Apply the function lower to all names in column 'Name' in df. Assign these new names to a new
# column of df called 'Lowercase Name'.


from string import lower
import pandas as pd

df = pd.DataFrame(
    [
        ["JOHN SMITH", "john.smith@gmail.com"],
        ["Jane Doe", "jdoe@yahoo.com"],
        ["joe schmo", "joeschmo@hotmail.com"],
    ],
    columns=["Name", "Email"],
)

df["Lowercase Name"] = df.Name.apply(lower)

print(df)

