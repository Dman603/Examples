import json as json
import numpy as np
from matplotlib import pyplot as plt
import math


def soe(n):
    arr = []
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n+1):
        if prime[p]:
            arr.append(p)
    return arr
allprimes = soe(200)

def counting_primes():
    arr = np.zeros([200,200])
    for item in allprimes: arr[item,item] = 1
    for i in range(4,200):
        j = 0
        while allprimes[j] <= math.floor((i)/2):
            arr[i,allprimes[j]] = sum(arr[i-allprimes[j],allprimes[j]:])
            j+=1
    return sum(arr[71])

print(counting_primes())