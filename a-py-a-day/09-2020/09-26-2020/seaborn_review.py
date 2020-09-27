"""
Seaborn is a Python data visualization library that provides simple code to create elegant visualizations for
statistical exploration and insight. Seaborn is based on Matplotlib, but improves on Matplotlib in several ways:

Seaborn provides a more visually appealing plotting style and concise syntax.
Seaborn natively understands Pandas DataFrames, making it easier to plot data directly from CSVs.
Seaborn can easily summarize Pandas DataFrames with many rows of data into aggregated charts.

If you’re unfamiliar with Pandas, just know that Pandas is a data analysis library for Python that provides easy-to-use
data structures and allows you to organize and manipulate datasets so they can be visualized. To fully leverage the
power of Seaborn, it is best to prepare your data using Pandas.

Over the next few exercises, we will explain how Seaborn relates to Pandas and how we can transform massive datasets
into easily understandable graphics.

"""

# The file script.py contains code to create a Seaborn visualization. Paste the following code at the very top of
# script.py to import Seaborn so that the code can run successfully:

import warnings

warnings.filterwarnings('ignore')
import pandas as pd
from matplotlib import pyplot as plt

import seaborn as sns

df = pd.read_csv('survey.csv')
sns.barplot(x='Age Range', y='Response', hue='Gender', data=df)
plt.show()

"""
Throughout this lesson, you’ll use Seaborn to visualize a Pandas DataFrame.

DataFrames contain data structured into rows and columns. DataFrames look similar to other data tables you may be
familiar with, but they are designed specifically to be used with Python.

You can create a DataFrame from a local CSV file (CSV files store data in a tabular format).

To create a DataFrame from a local CSV file you would use the syntax:

df = pd.read_csv('file_name.csv')
The code above creates a DataFrame saved to a variable named df. The data inside of the df DataFrame comes from the
data in the local CSV file named file_name.csv.

Once you have prepared and organized a Pandas DataFrame with your chosen dataset, you are ready to plot with Seaborn!

"""

# In script.py you can see pd.read_csv() is used to ingest the data stored in a file named survey.csv. If you’d like,
# you can inspect the contents of survey.csv in the file system of your workspace. We will explain the context of
# survey.csv in more detail in the next exercise. Focus on the syntax used to create a DataFrame from a CSV file.

# Inspect the DataFrame by printing the first 5 rows of df.

import warnings

warnings.filterwarnings('ignore')
import pandas as pd

df = pd.read_csv('survey.csv')
