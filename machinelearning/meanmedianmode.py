# What can we learn from looking at a group of numbers?
#
# In Machine Learning (and in mathematics) there are often three values that interests us:
#
# Mean - The average value
# Median - The mid point value
# Mode - The most common value

# mean

import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)

# medium

import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)

# mode Use the SciPy mode() method to find the number that appears the most:

from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)