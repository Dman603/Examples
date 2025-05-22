import numpy as np
from matplotlib import pyplot as plt
import math

### Could make this faster with numpy arrays or the set object I think. Its still quick enough though.

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
allprimes = soe(10000)
allprimes = np.array([item for item in allprimes if item<math.sqrt(50000000)]) # all our primes must be under 50,000,000^0.5 to apply

def primePowerTriples(b):
    cnt = 0
    arr = [False for i in range(50000000)]
    squares = [item**2 for item in allprimes if item**2 < b]
    cubes = [item**3 for item in allprimes if item**3 < b]
    quarts = [item**4 for item in allprimes if item**4 < b]
    for q in quarts:
        cu = [item for item in cubes if item < b - q]
        for c in cu:
            sq = [item for item in squares if item < b - q - c]
            for s in sq:
                if arr[s+c+q-1]:
                    cnt += 0
                else:
                    arr[s+c+q-1] = True
                    cnt+=1
    return (cnt)

print(primePowerTriples(50000000))