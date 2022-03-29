# Python program to print nxn assuming that n is always even

import numpy as np
def printcheckerboard(n):
    final = []
    for i in range(n):
        final.append(list(np.tile([0,1],int(n/2))) if i%2==0 else list(np.tile([1,0],int(n/2))))
    print(np.array(final))

# driver code
n = 8
printcheckerboard(n)