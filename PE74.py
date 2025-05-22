import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

### Problem statement at this link: https://projecteuler.net/problem=74

factorials = [1,1,2,6,24,120,720,5040,40320,362880]
def digit_factorial_sums():
    total = 0
    for i in range(10,1000001):
        if i%10000==0: print(i)
        n = i
        nums = [n]
        for j in range(60):
            s = 0
            for dig in str(n):
                s+=factorials[int(dig)]
            n = s
            if n not in nums and j<59:
                nums.append(n)
            elif n in nums and j==59:
                total+=1
            else:
                break
    return total

print(digit_factorial_sums())

            

