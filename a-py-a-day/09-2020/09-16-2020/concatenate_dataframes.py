"""
Concatenate DataFrames

Sometimes, a dataset is broken into multiple tables. For instance, data is often split into multiple CSV files so that each download is smaller.

When we need to reconstruct a single DataFrame from multiple smaller DataFrames, we can use the method pd.concat([df1, df2, df2, ...]). This method only works if all of the columns are the same in all of the DataFrames.

For instance, suppose that we have two DataFrames:
df1
name	email
Katja Obinger	k.obinger@gmail.com
Alison Hendrix	alisonH@yahoo.com
Cosima Niehaus	cosi.niehaus@gmail.com
Rachel Duncan	rachelduncan@hotmail.com
df2
name	email
Jean Gray	jgray@netscape.net
Scott Summers	ssummers@gmail.com
Kitty Pryde	kitkat@gmail.com
Charles Xavier	cxavier@hotmail.com

If we want to combine these two DataFrames, we can use the following command:

pd.concat([df1, df2])

That would result in the following DataFrame:
name	email
Katja Obinger	k.obinger@gmail.com
Alison Hendrix	alisonH@yahoo.com
Cosima Niehaus	cosi.niehaus@gmail.com
Rachel Duncan	rachelduncan@hotmail.com
Jean Gray	jgray@netscape.net
Scott Summers	ssummers@gmail.com
Kitty Pryde	kitkat@gmail.com
Charles Xavier	cxavier@hotmail.com

"""

# An ice cream parlor and a bakery have decided to merge.
#
# The bakery’s menu is stored in the DataFrame bakery, and the ice cream parlor’s menu is stored in DataFrame ice_cream.
#
# Create their new menu by concatenating the two DataFrames into a DataFrame called menu.

import pandas as pd

bakery = pd.read_csv('bakery.csv')
print(bakery)
ice_cream = pd.read_csv('ice_cream.csv')
print(ice_cream)

menu = pd.concat([bakery, ice_cream])
