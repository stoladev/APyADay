"""
When we get our data from other sources, we often want to change the column names. For example, we
might want all of the column names to follow variable name rules, so that we can use df.column_name
(which tab-completes) rather than df['column_name'] (which takes up extra space).

You can change all of the column names at once by setting the .columns property to a different list.
This is great when you need to change all of the column names at once, but be careful! You can
easily mislabel columns if you get the ordering wrong. Here’s an example:

df = pd.DataFrame({
    'name': ['John', 'Jane', 'Sue', 'Fred'],
    'age': [23, 29, 21, 18]
})
df.columns = ['First Name', 'Age']

        This command edits the existing DataFrame df.

"""

# The DataFrame df contains data about movies from IMDb.

# We want to present this data to some film producers, Our column names are in lower case,
# and are not very descriptive. Let’s modify df using the .columns attribute to make the following
# changes to the columns:

# Old     New
# id  ID
# name    Title
# genre   Category
# year    Year Released
# imdb_rating     Rating
# Concept Review

import pandas as pd

df = pd.read_csv("imdb.csv")

df.columns = ["ID", "Title", "Category", "Year Released", "Rating"]

print(df)

"""
You also can rename individual columns by using the .rename method. Pass a dictionary like the one
below to the columns keyword argument:

{'old_column_name1': 'new_column_name1', 'old_column_name2': 'new_column_name2'}

Here’s an example:

df = pd.DataFrame({
    'name': ['John', 'Jane', 'Sue', 'Fred'],
    'age': [23, 29, 21, 18]
})

df.rename(columns={
    'name': 'First Name',
    'age': 'Age'},
    inplace=True)

The code above will rename name to First Name and age to Age.

Using rename with only the columns keyword will create a new DataFrame, leaving
your original DataFrame unchanged. That’s why we also passed in the keyword
argument inplace=True. Using inplace=True lets us edit the original DataFrame.

There are several reasons why .rename is preferable to .columns:

You can rename just one column
You can be specific about which column names are getting changed (with .column you can
accidentally switch column names if you’re not careful)

*Note: *If you misspell one of the original column names, this command won’t fail. It just
won’t change anything.

"""

# If we didn’t know that df was a table of movie ratings, the column name might be confusing.

# To clarify, let’s rename name to movie_title.

# Use the keyword inplace=True so that you modify df rather than creating a new DataFrame!


import pandas as pd

df = pd.read_csv("imdb.csv")

df.rename(columns={"name": "movie_title"}, inplace=True)

print(df)

