"""
As we saw in the previous exercises, while it’s possible to plot multiple histograms, it is not a great option for
comparing distributions. Seaborn gives us another option for comparing distributions - a violin plot. Violin plots
provide more information than box plots because instead of mapping each individual data point, we get an estimation
of the dataset thanks to the KDE.

Violin plots are less familiar and trickier to read, so let’s break down the different parts:

There are two KDE plots that are symmetrical along the center line.
A white dot represents the median.
The thick black line in the center of each violin represents the interquartile range.
The lines that extend from the center are the confidence intervals - just as we saw on the bar plots, a violin plot
also displays the 95% confidence interval.

Violin Plots are a powerful graphing tool that allows you to compare multiple distributions at once.

Let’s look at how our original three data sets look like as violin plots:

sns.violinplot(data=df, x="label", y="value")
plt.show()
alt

As we can see, violin plots allow us to graph and compare multiple distributions. It also retains the shape of the
distributions, so we can easily tell that Dataset 1 is skewed left and that Dataset 3 is bimodal.

To plot a violin plot in Seaborn, use the method sns.violinplot().

There are several options for passing in relevant data to the x and y parameters:

data - the dataset that we’re plotting, such as a list, DataFrame, or array
x, y, and hue - a one-dimensional set of data, such as a Series, list, or array
any of the parameters to the function sns.boxplot()

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

sns.violinplot(data=df, x='label', y='value')
plt.show()

# Using sns.violinplot(), plot the four datasets as violin plots.
