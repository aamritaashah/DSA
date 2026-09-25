
# create array using array:

import numpy as np
a = np.array([1, 2, 3, 4, 5],int)
print(a)


import numpy as np
a = np.array([1.1,2.2,3.3,4.4,5.5],float)
print(a)

import numpy as np
a = np.array(['a','b','c','d','e'])
print(a)

import numpy as np
a = np.array(['Ujjval','Rohit','Bhuvan','Avinash','Abhisek'],dtype=str)
print(a)



#create array using linspace:

from numpy import linspace
a = linspace(1, 5, 5)
print(a)

from numpy import linspace
a = linspace(0, 10, 5)
print(a)



#create array using logspace:

from numpy import logspace
a = logspace(1,5,5)
a = logspace(1,5)
print(a)



# create array using arange:

from numpy import arange
a = arange(5)
print(a)

a = arange(1, 6)
print(a)

a = arange(1, 10, 2)
print(a)



# create array using zeros:

from numpy import zeros
a = zeros(5)
print(a)



#create array using ones:

from numpy import ones
a = ones(5)
print(a)


