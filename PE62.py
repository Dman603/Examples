import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

### Problem statement at this link: https://projecteuler.net/problem=62

def cubic_permutations():
    cubes = [sorted(str(k**3)) for k in range(10000)]
    for i in range(1,30000):
        cnt = 0
        srted = sorted(str(i**3))
        for cube in cubes[i:math.ceil(i*math.pow(10,1/3))]:
            if srted==cube: cnt+=1

        if cnt==5: return i

print(cubic_permutations())
