import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

### Problem statement at this link: https://projecteuler.net/problem=85

def CountingRect():
    minrect = 10000
    rect = 0
    for n in range(1,10000):
        for m in range(1,10000):
            count = 1/4 * (n**2+n)*(m**2+m)
            if abs(2000000-count)<minrect:
                minrect = abs(2000000-count)
                rect = n*m
            if n*m>2000000: break
    return rect, minrect

print(CountingRect())
