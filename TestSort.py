import numpy as np
from quicksortex import *

A = np.random.randint(20,size=10)
# A = np.array([5,5])
print A
sortedA = quicksortex(A)
print sortedA