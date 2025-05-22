import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

def square_root_convergents():
    cnt = 0
    n = 3
    d = 2
    for i in range(1,1001):
        if math.floor(math.log10(n))>math.floor(math.log10(d)): cnt+=1
        newd = n+d
        newn = 2*d + n
        n = newn
        d = newd
    return cnt

print(square_root_convergents())

