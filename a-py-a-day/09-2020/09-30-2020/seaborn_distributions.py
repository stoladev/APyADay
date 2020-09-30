"""
Here is a bar chart that uses three different randomly generated sets of data:

sns.barplot(data=df, x="label", y="value")
plt.show()
alt

These three datasets look identical! As far as we can tell, they each have the same mean and similar confidence
intervals.

We can get a lot of information from these bar charts, but we can’t get everything. For example, what are the minimum
and maximum values of these datasets? How spread out is this data?

While we may not see this information in our bar chart, these differences might be significant and worth understanding
better.

"""

import numpy as np
import pandas as pd
import seaborn as sns

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

sns.barplot(data=df, x='label', y='value')

# You work as a scientist and are measuring the amounts of plastic in different bodies of water. You’re interested in
# comparing data collected from different locations.
#
# We’ve imported four different datasets using NumPy and have combined them into one DataFrame, df.
#
# Use sns.barplot() to graph the datasets in one plot, with "label" as the x data and "value" as the y data.
