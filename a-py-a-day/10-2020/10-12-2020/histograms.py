"""
When we first look at a dataset, we want to be able to quickly understand certain things about it:

Do some values occur more often than others?
What is the range of the dataset (i.e., the min and the max values)?
Are there a lot of outliers?
We can visualize this information using a chart called a histogram.

For instance, suppose that we have the following dataset:

d = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5]
A simple histogram might show us how many 1’s, 2’s, 3’s, etc. we have in this dataset.

Value	Number of Samples
1	3
2	5
3	2
4	4
5	1

Suppose we had a larger dataset with values ranging from 0 to 50. We might not want to know exactly
how many 0’s, 1’s, 2’s, etc. we have.

Instead, we might want to know how many values fall between 0 and 5, 6 and 10, 11 and 15, etc.

These groupings are called bins. All bins in a histogram are always the same size. The width of
each bin is the distance between the minimum and maximum values of each bin. In our example, the
width of each bin would be 5.

For a dataset like this, our histogram table would look like this:

Bin	Number of Values
(0, 5)	2
(6, 10)	10
(11, 15)	11
…	…
(46, 50)	3

We can graph histograms using a Python module known as Matplotlib. We’re not going to go into detail about Matplotlib’s plotting functions, but if you’re interested in learning more, take our course Introduction to Matplotlib.

For now, familiarize yourself with the following syntax to draw a histogram:

# This imports the plotting package.  We only need to do this once.
from matplotlib import pyplot as plt 

# This plots a histogram
plt.hist(data)

# This displays the histogram
plt.show()
When we enter plt.hist with no keyword arguments, matplotlib will automatically make a histogram
with 10 bins of equal width that span the entire range of our data.

If you want a different number of bins, use the keyword bins. For instance, the following code
would give us 5 bins, instead of 10:

plt.hist(data, bins=5)
If you want a different range, you can pass in the minimum and maximum values that you want to
histogram using the keyword range. We pass in a tuple of two numbers. The first number is the
minimum value that we want to plot and the second value is the number that we want to plot up to,
but not including.

For instance, if our dataset contained values between 0 and 100, but we only wanted to histogram
numbers between 20 and 50, we could use this command:

# We pass 51 so that our range includes 50
plt.hist(data, range=(20, 51))
Here’s a complete example:

from matplotlib import pyplot as plt

d = np.array([1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5])

plt.hist(d, bins=5, range=(1, 6))

plt.show()

"""

import numpy as np
# Write matplotlib import here:
from matplotlib import pyplot as plt

commutes = np.genfromtxt('commutes.csv', delimiter=',')

# Plot histogram here:
plt.hist(commutes, range=(20, 51), bins=6)


plt.show()

"""
Histograms and their datasets can be classified based on the shape of the graphed values. In the
next two exercises, we’ll look at two different ways of describing histograms.

One way to classify a dataset is by counting the number of distinct peaks present in the graph.
Peaks represent concentrations of data. Let’s look at the following examples:

A unimodal dataset has only one distinct peak.

A bimodal dataset has two distinct peaks. This often happens when the data contains two different
populations.

A multimodal dataset has more than two peaks.

A uniform dataset doesn’t have any distinct peaks.

Most of the datasets that we’ll be dealing with will be unimodal (one peak). We can further
classify unimodal distributions by describing where most of the numbers are relative to the peak.

A symmetric dataset has equal amounts of data on both sides of the peak. Both sides should look
about the same.

A skew-right dataset has a long tail on the right of the peak, but most of the data is on the left.

A skew-left dataset has a long tail on the left of the peak, but most of the data is on the right.

The type of distribution affects the position of the mean and median. In heavily skewed
distributions, the mean becomes a less useful measurement.

Normal Distribution, Part I
The most common distribution in statistics is known as the normal distribution, which is a
symmetric, unimodal distribution.

Lots of things follow a normal distribution:

The heights of a large group of people
Blood pressure measurements for a group of healthy people
Errors in measurements

Normal distributions are defined by their mean and standard deviation. The mean sets the “middle”
of the distribution, and the standard deviation sets the “width” of the distribution. A larger
standard deviation leads to a wider distribution. A smaller standard deviation leads to a skinnier
distribution.

We can generate our own normally distributed datasets using NumPy. Using these datasets can help
us better understand the properties and behavior of different distributions. We can also use
them to model results, which we can then use as a comparison to real data.

In order to create these datasets, we need to use a random number generator. The NumPy library has
several functions for generating random numbers, including one specifically built to generate a
set of numbers that fit a normal distribution: np.random.normal. This function takes the following
keyword arguments:

loc: the mean for the normal distribution
scale: the standard deviation of the distribution
size: the number of random numbers to generate
a = np.random.normal(0, 1, size=100000)

"""

# Our friend is a paleontologist. He’s studying two types of dinosaurs: brachiosaurus and
# fictionosaurus. He tells us that:

# Brachiosaurus have femurs (thigh bone) with mean length of 6.7 ft and a standard deviation of
# 0.7 ft.

# Fictionosaurus have femurs (thigh bone) with mean length of 7.7 ft and a standard deviation of
# 0.3 ft.

# We’d like to know what these distributions look like.

# Use np.random.normal to fill in b_data (brachiosaurus) and f_data (fictionosaurus) with randomly
# generated samples with the correct mean and standard deviation. Each dataset should have 1000
# samples.

# The code that we supplied below will graph the distributions for you.

import numpy as np
from matplotlib import pyplot as plt

# Brachiosaurus
b_data = np.random.normal(6.7, 0.7, size=1000)

# Fictionosaurus
f_data = np.random.normal(7.7, 0.3, size=1000)

plt.hist(b_data,
         bins=30, range=(5, 8.5), histtype='step',
         label='Brachiosaurus')
plt.hist(f_data,
         bins=30, range=(5, 8.5), histtype='step',
         label='Fictionosaurus')
plt.xlabel('Femur Length (ft)')
plt.legend(loc=2)
plt.show()

mystery_dino = 'brachiosaurus'

answer = False
