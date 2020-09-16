# NumPy is a python library used for working with arrays.
#
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
#
# NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.
#
# NumPy stands for Numerical Python.

# Why Use NumPy ?
# In Python we have lists that serve the purpose of arrays, but they are slow to process.
#
# NumPy aims to provide an array object that is up to 50x faster that traditional Python lists.
#
# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
#
# Arrays are very frequently used in data science, where speed and resources are very important.

import numpy

arr = numpy.array([1,2,3,4,5,])
print(arr)

# NumPy as np
# NumPy is usually imported under the np alias.
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

from numpy import random

x = random.randint(100)

print(x)