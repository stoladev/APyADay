"""
While a KDE plot can tell us about the shape of the data, it’s cumbersome to compare multiple KDE plots at once. They
also can’t tell us other statistical information, like the values of outliers.

The box plot (also known as a box-and-whisker plot) can’t tell us about how our dataset is distributed, like a KDE
plot. But it shows us the range of our dataset, gives us an idea about where a significant portion of our data lies,
and whether or not any outliers are present.

Let’s examine how we interpret a box plot:

The box represents the interquartile range
The line in the middle of the box is the median
The end lines are the first and third quartiles
The diamonds show outliers

One advantage of the box plot over the KDE plot is that in Seaborn, it is easy to plot multiples and compare
distributions.

Let’s look again at our three datasets, and how they look plotted as box plots:

sns.boxplot(data=df, x='label', y='value')
plt.show()
alt

The box plot does a good job of showing certain differences, the different between Dataset 1 and Dataset 2; however,
it does not show that Dataset 3 is bimodal.

To plot a box plot in Seaborn, we use the method sns.boxplot().

A box plot takes the following arguments:

data - the dataset we’re plotting, like a DataFrame, list, or an array
x - a one-dimensional set of values, like a Series, list, or array
y - a second set of one-dimensional data
If you use a Pandas Series for the x and y values, the Series will also generate the axis labels. For example, if you
use the value Series as your y value data, Seaborn will automatically apply that name as the y-axis label.

"""

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Take in the data from the CSVs as NumPy arrays:
set_one = np.genfromtxt("dataset1.csv", delimiter=",")
set_two = np.genfromtxt("dataset2.csv", delimiter=",")
set_three = np.genfromtxt("dataset3.csv", delimiter=",")
set_four = np.genfromtxt("dataset4.csv", delimiter=",")

# Creating a Pandas DataFrame:
n = 500
df = pd.DataFrame({
    "label": ["set_one"] * n + ["set_two"] * n + ["set_three"] * n + ["set_four"] * n,
    "value": np.concatenate([set_one, set_two, set_three, set_four])
})

# Setting styles:
sns.set_style("darkgrid")
sns.set_palette("pastel")

sns.boxplot(data=df, x='label', y='value')
plt.show()

# Use sns.boxplot() to plot the four datasets as box plots.
