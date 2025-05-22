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
allprimes = soe(1000000)



def totient_perm(ind, baseline):
    index = ind
    minph = baseline
    minp = 0
    while allprimes[index]**2 < 10**7:
        i = 0
        print(index)
        while allprimes[index]*allprimes[index+i] < 10**7:
            if sorted(str(allprimes[index]*allprimes[index+i])) == sorted(str(allprimes[index]*allprimes[index+i]+ 1 - allprimes[index] - allprimes[index+i])):
                if (allprimes[index]*allprimes[index+i])/(allprimes[index]*allprimes[index+i]-allprimes[index]-allprimes[index+i]+1)<minph:
                    minph = (allprimes[index]*allprimes[index+i])/(allprimes[index]*allprimes[index+i]-allprimes[index]-allprimes[index+i]+1)
                    minp = allprimes[index]*allprimes[index+i]
            i+=1
        index+=1
    return minp, minph

print(totient_perm(10,1.1))
