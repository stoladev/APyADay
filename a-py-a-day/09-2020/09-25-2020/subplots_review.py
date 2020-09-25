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

"""
We are going to create a figure that has two rows of subplots. It should have:

    one subplot in the top row
    two subplots in the bottom row

Start by using the subplot method to instantiate the subplot in the top row (the box with the star in it).
"""

from matplotlib import pyplot as plt

x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

plt.subplot(2, 1, 1)
plt.plot(x, straight_line)

# Subplot 2
plt.subplot(2, 2, 3)
plt.plot(x, parabola)

# Subplot 3
plt.subplot(2, 2, 4)
plt.plot(x, cubic)

plt.subplots_adjust(wspace=0.35, bottom=0.2)

plt.show()

"""
When we have multiple lines on a single graph we can label them by using the command plt.legend().

The legend method takes a list with the labels to display. So, for example, we can call:

plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64])
plt.legend(['parabola', 'cubic'])
plt.show()

 plt.legend() can also take a keyword argument loc, which will position the legend on the figure.

These are the position values loc accepts:
Number Code 	String
0 	best
1 	upper right
2 	upper left
3 	lower left
4 	lower right
5 	right
6 	center left
7 	center right
8 	lower center
9 	upper center
10 	center

Note: If you decide not to set a value for loc, it will default to choosing the “best” location.

For, example, we can call plt.legend() and set loc to 6:

plt.legend(['parabola', 'cubic'], loc=6)
plt.show()

Sometimes, it’s easier to label each line as we create it. If we want, we can use the keyword label inside of
plt.plot(). If we choose to do this, we don’t pass any labels into plt.legend(). For example:

plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16],
         label="parabola")
plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64],
         label="cubic")
plt.legend() # Still need this command!
plt.show()

"""

months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]

plt.plot(months, hyrule)
plt.plot(months, kakariko)
plt.plot(months, gerudo)

# create your legend here
legend_labels = ["Hyrule", "Kakariko", "Gerudo Valley"]
plt.legend(legend_labels, loc=8)

plt.show()

"""
Modify Ticks

In all of our previous exercises, our commands have started with plt.. In order to modify tick marks, we’ll have to try
something a little bit different.

Because our plots can have multiple subplots, we have to specify which one we want to modify. In order to do that, we
call plt.subplot() in a different way.

ax = plt.subplot(1, 1, 1)

ax is an axes object, and it lets us modify the axes belonging to a specific subplot. Even if we only have one subplot,
when we want to modify the ticks, we will need to start by calling either ax = plt.subplot(1, 1, 1) or ax =
plt.subplot() in order to get our axes object.

Suppose we wanted to set our x-ticks to be at 1, 2, and 4. We would use the following code:

ax = plt.subplot()
plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64])
ax.set_xticks([1, 2, 4])

e can also modify the y-ticks by using ax.set_yticks().

When we change the x-ticks, their labels automatically change to match. But, if we want special labels
(such as strings), we can use the command ax.set_xticklabels() or ax.set_yticklabels(). For example, we might want to
have a y-axis with ticks at 0.1, 0.6, and 0.8, but label them 10%, 60%, and 80%, respectively. To do this, we use the
following commands:

ax = plt.subplot()
plt.plot([1, 3, 3.5], [0.1, 0.6, 0.8], 'o')
ax.set_yticks([0.1, 0.6, 0.8])
ax.set_yticklabels(['10%', '60%', '80%'])

"""

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

months = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]

plt.xlabel("Months")
plt.ylabel("Conversion")

plt.plot(months, conversion)

# Your work here
ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)
ax.set_yticks([0.10, 0.25, 0.5, 0.75])
ax.set_yticklabels(["10%", "25%", "50%", "75%"])

plt.show()

"""
When we’re making lots of plots, it’s easy to end up with lines that have been plotted and not displayed. If we’re not
careful, these “forgotten” lines will show up in your new plots. In order to be sure that you don’t have any stray
lines, you can use the command plt.close('all') to clear all existing plots before you plot a new one.

Previously, we learned how to put two sets of axes into the same figure. Sometimes, we would rather have two separate
figures. We can use the command plt.figure() to create new figures and size them how we want. We can add the keyword
figsize=(width, height) to set the size of the figure, in inches. We use parentheses (( and )) to pass in the width and
height, which are separated by a comma (,).

To create a figure with a width of 4 inches, and height of 10 inches, we would use:

plt.figure(figsize=(4, 10))

Once we’ve created a figure, we might want to save it so that we can use it in a presentation or a website. We can use
the command plt.savefig() to save out to many different file formats, such as png, svg, or pdf. After plotting, we can
call plt.savefig('name_of_graph.png'):

# Figure 2
plt.figure(figsize=(4, 10)) 
plt.plot(x, parabola)
plt.savefig('tall_and_narrow.png')

This will save tall_and_narrow.png to our file system.

"""

word_length = [8, 11, 12, 11, 13, 12, 9, 9, 7, 9]
power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

plt.close('all')
plt.figure()
plt.plot(years, word_length)
plt.savefig('winning_word_lengths.png')
plt.figure(figsize=(7, 3))
plt.plot(years, power_generated)
plt.savefig('power_generated.png')

x = range(6)
y1 = [1, 2, 3, 4, 5, 6]
y2 = [-1, 1, 3, 4, 4, 4]

plt.plot(x, y1, marker='o', color='pink')
plt.plot(x, y2, marker='o', color='gray')

plt.title("Two Lines on One Graph")
plt.xlabel("Amazing X-axis")
plt.ylabel("Incredible Y-axis")

plt.legend(["Y1", "Y2"], loc=4)

plt.show()
