import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

### Problem statement at this link: https://projecteuler.net/problem=52

def permuted_multiples():
    for b in range(2,8):
        for i in range(1,(10**b)//6):
            s = sorted(str(i))
            b = True
            for j in range(2,7):
                if sorted(str(i*j))!=s:
                    b = False
                    break
            if b:
                return i

print(permuted_multiples())

