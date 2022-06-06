import numpy as np
from numpy import random

size1 = int(input("How big?"))
min1 = int(input("Smallest number?"))
max1 = int(input("Biggest Number?"))

c = random.randint(min1,max1,size1)
c

a = c.min()
a
b = c.max()
b
size2 = c.size
ave1 = c.sum()/size2
ave1
