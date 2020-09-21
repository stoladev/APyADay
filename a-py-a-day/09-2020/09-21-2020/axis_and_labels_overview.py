"""
Sometimes, it can be helpful to zoom in or out of the plot, especially if there is some detail we want to address. To
zoom, we can use plt.axis(). We use plt.axis() by feeding it a list as input. This list should contain:

    The minimum x-value displayed
    The maximum x-value displayed
    The minimum y-value displayed
    The maximum y-value displayed

For example, if we want to display a plot from x=0 to x=3 and from y=2 to y=5, we would call plt.axis([0, 3, 2, 5]).

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
plt.plot(x, y)
plt.axis([0, 3, 2, 5])
plt.show()

axis_zoom

"""

# Let’s modify the axes to zoom in a bit more on our line chart. Use plt.axis() to modify the axes so that the x-axis
# goes from 0 to 12, and the y-axis goes from 2900 to 3100.

from matplotlib import pyplot as plt

x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)

plt.axis([0, 12, 2900, 3100])

plt.show()

"""
The first step towards a professional-looking plot is adding labels to the x-axis and y-axis, and giving the plot a
title.

We can label the x- and y- axes by using plt.xlabel() and plt.ylabel(). The plot title can be set by using plt.title().

All of these commands require a string, which is a set of characters in either single (') or double (") quotes.

"This is a string"
'This is also a string'

'This is NOT a string (the quotes do not match)"

For example, if someone has been keeping track of their happiness (on a scale out of 10) throughout the day and wants
to display this information with labeled axes, we can use the following commands:

hours = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
happiness = [9.8, 9.9, 9.2, 8.6, 8.3, 9.0, 8.7, 9.1, 7.0, 6.4, 6.9, 7.5]
plt.plot(hours, happiness)
plt.xlabel('Time of day')
plt.ylabel('Happiness Rating (out of 10)')
plt.title('My Self-Reported Happiness While Awake')
plt.show()

"""

# Label the x-axis 'Time'.

plt.xlabel('Time')
plt.ylabel('Dollars spent on coffee')
plt.title('My Last Twelve Years of Coffee Drinking')

"""
Sometimes, we want to display two lines side-by-side, rather than in the same set of x- and y-axes. When we have
multiple axes in the same picture, we call each set of axes a subplot. The picture or object that contains all of the
subplots is called a figure.

We can have many different subplots in the same figure, and we can lay them out in many different ways. We can think of
our layouts as having rows and columns of subplots. For instance, the following figure has six subplots split into 2
rows and 3 columns:

We can create subplots using .subplot().

The command plt.subplot() needs three arguments to be passed into it:

    The number of rows of subplots
    The number of columns of subplots
    The index of the subplot we want to create

For instance, the command plt.subplot(2, 3, 4) would create “Subplot 4” from the figure above.

Any plt.plot() that comes after plt.subplot() will create a line plot in the specified subplot. For instance:

# Data sets
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

# First Subplot
plt.subplot(1, 2, 1)
plt.plot(x, y, color='green')
plt.title('First Subplot')

# Second Subplot
plt.subplot(1, 2, 2)
plt.plot(x, y, color='steelblue')
plt.title('Second Subplot')

# Display both subplots
plt.show()

"""

# We have defined the lists months, temperature, and flights_to_hawaii for you. Using the plt.subplot command, plot
# temperature vs months in the left box of a figure that has 1 row with 2 columns.

months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

plt.subplot(1, 2, 1)

"""
We can customize the spacing between our subplots to make sure that the figure we create is visible and easy to
understand. To do this, we use the plt.subplots_adjust() command. .subplots_adjust() has some keyword arguments that
can move your plots within the figure:

    left — the left-side margin, with a default of 0.125. You can increase this number to make room for a y-axis label
    right — the right-side margin, with a default of 0.9. You can increase this to make more room for the figure, or
    decrease it to make room for a legend
    bottom — the bottom margin, with a default of 0.1. You can increase this to make room for tick mark labels or an
    x-axis label
    top — the top margin, with a default of 0.9
    wspace — the horizontal space between adjacent subplots, with a default of 0.2
    hspace — the vertical space between adjacent subplots, with a default of 0.2

For example, if we were adding space to the bottom of a graph by changing the bottom margin to 0.2 (instead of the
default of 0.1), we would use the command:

plt.subplots_adjust(bottom=0.2)

We can also use multiple keyword arguments, if we need to adjust multiple margins. For instance, we could adjust both
the top and the hspace:

plt.subplots_adjust(top=0.95, hspace=0.25)

Let’s use wspace to fix the figure above:

# Left Plot
plt.subplot(1, 2, 1)
plt.plot([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4])

# Right Plot
plt.subplot(1, 2, 2)
plt.plot([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4])

# Subplot Adjust
plt.subplots_adjust(wspace=0.35)

plt.show()

"""
