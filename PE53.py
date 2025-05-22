import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

### Problem statement at this link: https://projecteuler.net/problem=53


def combinatoric_selections():
    cnt = 0
    for i in range(1,101):
        for j in range(1,i):
            if math.comb(i,j) >= 10**6:
                cnt+=1
    return cnt

print(combinatoric_selections())

