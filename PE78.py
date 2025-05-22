import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

### Problem statement at this link: https://projecteuler.net/problem=78

### wikipedia article on integer partitions is a must read otherwise this problem is impossible because you are not leonhard euler

def coin_partitions():
    arr = np.array([1,1])
    pent = ([(3*k**2-k)//2 for k in range(-2000,2000)])
    pent.sort()
    for i in range(2,2000000):
        if i%10000==0: print(i)
        su = 0
        k = 1
        while pent[k] <= i:
            if k%4 == 1 or k%4 == 2:
                su = su + arr[i-pent[k]]
            else: su = su - arr[i-pent[k]]
            k+=1
        n = su%1000000
        if(n==0): return "THIS IS THE NUMBER:" + str(i)
        arr = np.append(arr,n)
    return arr[1990000:2000000]

print(coin_partitions())
