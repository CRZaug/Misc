# Check if a vector is sorted using recursion

import numpy as np

#vector = np.random.randint(10,size=10)
#vector = [6, 9, 3, 0, 4, 6, 3, 2, 1, 4]
#vector = [1,4]
vector = [0,1,2,3,4,5,6,7,8,9]

print(vector)

def f(vect):

    if len(vect)>1:
        a=vect[-1]
        vectnew = vect[:-1]
        b = vectnew[-1]
        if a>=b:
            return f(vectnew)
        else:
            return False
    else:
        return True

var = f(vector)

print(bool(var))
