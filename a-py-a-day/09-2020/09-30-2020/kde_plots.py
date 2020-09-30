"""
Bar plots can tell us what the mean of our dataset is, but they don’t give us any hints as to the distribution of the
dataset values. For all we know, the data could be clustered around the mean or spread out evenly across the entire
range.

To find out more about each of these datasets, we’ll need to examine their distributions. A common way of doing so is
by plotting the data as a histogram, but histograms have their drawback as well.

Seaborn offers another option for graphing distributions: KDE Plots.

KDE stands for Kernel Density Estimator. A KDE plot gives us the sense of a univariate as a curve. A univariate dataset
only has one variable and is also referred to as being one-dimensional, as opposed to bivariate or two-dimensional
datasets which have two variables.

KDE plots are preferable to histograms because depending on how you group the data into bins and the width of the bins,
you can draw wildly different conclusions about the shape of the data. Using a KDE plot can mitigate these issues,
because they smooth the datasets, allow us to generalize over the shape of our data, and aren’t beholden to specific
data points.

To plot a KDE in Seaborn, we use the method sns.kdeplot().

A KDE plot takes the following arguments:

data - the univariate dataset being visualized, like a Pandas DataFrame, Python list, or NumPy array
shade - a boolean that determines whether or not the space underneath the curve is shaded
Let’s examine the KDE plots of our three datasets:

sns.kdeplot(dataset1, shade=True)
sns.kdeplot(dataset2, shade=True)
sns.kdeplot(dataset3, shade=True)
plt.legend()
plt.show()
alt

Notice that when using a KDE we need to plot each of the original datasets separately, rather than using a combined
dataframe like we did with the bar plot.

It looks like there are some big differences between the three datasets:

Dataset 1 is skewed left
Dataset 2 is normally distributed
Dataset 3 is bimodal (it has two peaks)
So although all three datasets have roughly the same mean, the shapes of the KDE plots demonstrate the differences in
how the values are distributed.

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

sns.kdeplot(set_one, shade=True)
sns.kdeplot(set_two, shade=True)
sns.kdeplot(set_three, shade=True)
sns.kdeplot(set_four, shade=True)

# Use sns.kdeplot() to graph the four datasets and set shade to True.
