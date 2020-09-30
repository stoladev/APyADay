"""
Seaborn can also calculate aggregate statistics for large datasets. To understand why this is helpful, we must first
understand what an aggregate is.

An aggregate statistic, or aggregate, is a single number used to describe a set of data. One example of an aggregate is
the average, or mean of a data set. There are many other aggregate statistics as well.

Suppose we have a grade book with columns student, assignment_name, and grade, as shown below.

student	assignment_name	grade
Amy	Assignment 1	75
Amy	Assignment 2	82
Bob	Assignment 1	99
Bob	Assignment 2	90
Chris	Assignment 1	72
Chris	Assignment 2	66
…	…	…
To calculate a student’s current grade in the class, we need to aggregate the grade data by student. To do this, we’ll
calculate the average of each student’s grades, resulting in the following data set:

student	grade
Amy	78.5
Bob	94.5
Chris	69
…	…
On the other hand, we may be interested in understanding the relative difficulty of each assignment. In this case, we
would aggregate by assignment, taking the average of all student’s scores on each assignment:

assignment_name	grade
Assignment 1	82
Assignment 2	79.3
…	…
In both of these cases, the function we used to aggregate our data was the average or mean, but there are many types of
aggregate statistics including:

Median
Mode
Standard Deviation
In Python, you can compute aggregates fairly quickly and easily using Numpy, a popular Python library for computing.
You’ll use Numpy in this exercise to compute aggregates for a DataFrame.

"""

import warnings

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

gradebook = pd.read_csv('gradebook.csv')
print(gradebook)

assignment1 = gradebook[gradebook.assignment_name == 'Assignment 1']
print(assignment1)

asn1_median = np.median(assignment1.grade)
print(asn1_median)

"""

Plotting Aggregates
Recall our gradebook from the previous exercise:

student	assignment_name	grade
Amy	Assignment 1	75
Amy	Assignment 2	82
Bob	Assignment 1	99
Bob	Assignment 2	90
Chris	Assignment 1	72
Chris	Assignment 2	66
…	…	…

Suppose this data is stored in a Pandas DataFrame called df.

The same Seaborn command that you previously learned (sns.barplot()) will plot this data in a bar plot and automatically aggregate the data:

sns.barplot(data=df, x="student", y="grade")
In the example above, Seaborn will aggregate grades by student, and plot the average grade for each student.


"""

warnings.filterwarnings('ignore')

gradebook_2 = pd.read_csv("gradebook_2.csv")

sns.barplot(data=gradebook_2, x="assignment_name", y="grade")

plt.show()
