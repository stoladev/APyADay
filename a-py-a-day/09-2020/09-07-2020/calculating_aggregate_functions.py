"""
Calculating Aggregate Functions II

After using groupby, we often need to clean our resulting data.

As we saw in the previous exercise, the groupby function creates a new Series, not a DataFrame. For
our ShoeFly.com example, the indices of the Series were different values of shoe_type, and the name
property was price.

Usually, we’d prefer that those indices were actually a column. In order to get that, we can use
reset_index(). This will transform our Series into a DataFrame and move the indices into their own
column.

Generally, you’ll always see a groupby statement followed by reset_index

df.groupby('column1').column2.measurement()
.reset_index()

When we use groupby, we often want to rename the column we get as a result. For example, suppose
we have a DataFrame teas containing data on types of tea
id  tea     category    caffeine    price
0   earl grey   black   38  3
1   english breakfast   black   41  3
2   irish breakfast     black   37  2.5
3   jasmine     green   23  4.5
4   matcha  green   48  5
5   camomile    herbal  0   3

We want to find the number of each category of tea we sell. We can use

teas_counts = teas.groupby('category').id.count().reset_index()

This yields a DataFrame that looks like
category    id
0   black   3
1   green   4
2   herbal  8
3   white   2

The new column contains the counts of each category of tea sold. We have 3 black teas, 4
green teas, and so on. However, this column is called id because we used the id column
of teas to calculate the counts. We actually want to call this column counts. Remember
that we can rename columns

teas_counts = teas_counts.rename(columns={"id": "counts"})

Our DataFrame now looks like
category    counts
0   black   3
1   green   4
2   herbal  8
3   white   2

"""

import pandas as pd

orders = pd.read_csv("orders.csv")

pricey_shoes = orders.groupby("shoe_type").price.max().reset_index()

print(pricey_shoes)

print(type(pricey_shoes))

