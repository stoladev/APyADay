"""
By default, Seaborn will place error bars on each bar when you use the barplot() function.

Error bars are the small lines that extend above and below the top of each bar. Errors bars visually indicate the range
of values that might be expected for that bar.


For example, in our assignment average example, an error bar might indicate what grade we expect an average student to
receive on this assignment.


There are several different calculations that are commonly used to determine error bars.

By default, Seaborn uses something called a bootstrapped confidence interval. Roughly speaking, this interval means that
“based on this data, 95% of similar situations would have an outcome within this range”.

In our gradebook example, the confidence interval for the assignments means “if we gave this assignment to many, many
students, we’re confident that the mean score on the assignment would be within the range represented by the error bar”.

The confidence interval is a nice error bar measurement because it is defined for different types of aggregate
functions, such as medians and mode, in addition to means.

If you’re calculating a mean and would prefer to use standard deviation for your error bars, you can pass in the
keyword argument ci="sd" to sns.barplot() which will represent one standard deviation. It would look like this:

sns.barplot(data=gradebook, x="name", y="grade", ci="sd")

"""

# Modify the bar plot so that the error bars represent one standard deviation, rather than 95% confidence intervals.
import warnings

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

warnings.filterwarnings('ignore')

gradebook = pd.read_csv("gradebook.csv")

sns.barplot(data=gradebook, x="name", y="grade", ci="sd")
plt.show()

"""
In most cases, we’ll want to plot the mean of our data, but sometimes, we’ll want something different:

If our data has many outliers, we may want to plot the median.
If our data is categorical, we might want to count how many times each category appears (such as in the case of survey
responses).
Seaborn is flexible and can calculate any aggregate you want. To do so, you’ll need to use the keyword argument
estimator, which accepts any function that works on a list.

For example, to calculate the median, you can pass in np.median to the estimator keyword:

sns.barplot(data=df,
  x="x-values",
  y="y-values",
  estimator=np.median)
Consider the data in results.csv. To calculate the number of times a particular value appears in the Response column,
we pass in len:

sns.barplot(data=df,
  x="Patient ID",
  y="Response",
  estimator=len)

"""

# Consider our hospital satisfaction survey data, which is loaded into the Pandas DataFrame df. Use print to examine
# the data.

# We’d like to know how many men and women answered the survey. Use sns.barplot() with:
#
# data equal to df
# x equal to Gender
# y equal to Response
# estimator equal to len

# Use plt.show() to display the graph.

# Change sns.barplot() to graph the median Response aggregated by Gender using estimator=np.median.

warnings.filterwarnings('ignore')

df = pd.read_csv("survey.csv")
print(df)

# sns.barplot(data=df,
#            x='Gender',
#            y='Response',
#            estimator=len)

sns.barplot(data=df,
            x='Gender',
            y='Response',
            estimator=np.median)

plt.show()

"""
Sometimes we’ll want to aggregate our data by multiple columns to visualize nested categorical variables.

For example, consider our hospital survey data. The mean satisfaction seems to depend on Gender, but it might also
depend on another column: Age Range.

We can compare both the Gender and Age Range factors at once by using the keyword hue.

sns.barplot(data=df,
            x="Gender",
            y="Response",
            hue="Age Range")
The hue parameter adds a nested categorical variable to the plot.

*Visualizing survey results by gender with age range nested*.
Notice that we keep the same x-labels, but we now have different color bars representing each Age Range. We can
compare two bars of the same color to see how patients with the same Age Range, but different Gender rated the survey.

"""

# Use plt.show() to display the graph.

df = pd.read_csv("survey.csv")

sns.barplot(data=df,
            x="Age Range",
            y="Response",
            hue="Gender")

plt.show()

"""
To review the seaborn workflow:

1. Ingest data from a CSV file to Pandas DataFrame.
df = pd.read_csv('file_name.csv')

2. Set sns.barplot() with desired values for x, y, and set data equal to your DataFrame.
sns.barplot(data=df, x='X-Values', y='Y-Values')

3. Set desired values for estimator and hue parameters.
sns.barplot(data=df, x='X-Values', y='Y-Values', estimator=len, hue='Value')

4. Render the plot using plt.show().
plt.show()

"""
