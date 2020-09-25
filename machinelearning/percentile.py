# What are Percentiles?
# Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.
#
# Example: Let's say we have an array of the ages of all the people that lives in a street.

# Example: Let's say we have an array of the ages of all the people that lives in a street.
#
# ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
#
# What is the 75. percentile? The answer is 43, meaning that 75% of the people are 43 or younger.
#
# The NumPy module has a method for finding the specified percentile:

import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 75)

print(x)

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
z = numpy.percentile(ages, 90)

print(z)