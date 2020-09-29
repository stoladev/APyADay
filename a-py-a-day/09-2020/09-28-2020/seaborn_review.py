"""
DataFrames contain data structured into rows and columns. DataFrames look similar to other data tables you may be
familiar with, but they are designed specifically to be used with Python.

You can create a DataFrame from a local CSV file (CSV files store data in a tabular format).

To create a DataFrame from a local CSV file you would use the syntax:

df = pd.read_csv('file_name.csv')
The code above creates a DataFrame saved to a variable named df. The data inside of the df DataFrame comes from the
data in the local CSV file named file_name.csv.

"""

# In script.py you can see pd.read_csv() is used to ingest the data stored in a file named survey.csv. If you’d like,
# you can inspect the contents of survey.csv in the file system of your workspace. We will explain the context of
# survey.csv in more detail in the next exercise. For now, focus on the syntax used to create a DataFrame from a
# CSV file.
#
# Inspect the DataFrame by printing the first 5 rows of df.

import warnings

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

warnings.filterwarnings('ignore')

df = pd.read_csv('survey.csv')

print(df.head())

"""
Suppose we are analyzing data from a survey: we asked 1,000 patients at a hospital how satisfied they were with their experience. Their response was measured on a scale of 1 - 10, with 1 being extremely unsatisfied, and 10 being extremely satisfied. We have summarized that data in a CSV file called results.csv.

To plot this data using Matplotlib, you would write the following:

df = pd.read_csv("results.csv")
ax = plt.subplot()
plt.bar(range(len(df)),
        df["Mean Satisfaction"])
ax.set_xticks(range(len(df)))
ax.set_xticklabels(df.Gender)
plt.xlabel("Gender")
plt.ylabel("Mean Satisfaction")

That’s a lot of work for a simple bar chart! Seaborn gives us a much simpler option. With Seaborn, you can use the
sns.barplot() command to do the same thing.

The Seaborn function sns.barplot(), takes at least three keyword arguments:

data: a Pandas DataFrame that contains the data (in this example, data=df)
x: a string that tells Seaborn which column in the DataFrame contains otheur x-labels (in this case, x="Gender")
y: a string that tells Seaborn which column in the DataFrame contains the heights we want to plot for each bar (in this
case y="Mean Satisfaction")
By default, Seaborn will aggregate and plot the mean of each category. In the next exercise you will learn more about
aggregation and how Seaborn handles it.

"""

# Use Pandas to load in the data from results.csv and save it to the variable df.
# Display df using print
# Remove all of the # characters from in front of the sns.barplot command and fill in the missing values.
# Type plt.show() to display the completed bar plot.


warnings.filterwarnings('ignore')

# Load results.csv here:
df = pd.read_csv('results.csv')
print(df)

sns.barplot(
    data=df,
    x='Gender',
    y='Mean Satisfaction'
)

plt.show()
