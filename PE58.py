import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

### Problem statement at this link: https://projecteuler.net/problem=58

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

def isprime(n):
    i = 0
    if n == 1:
        return False
    while math.sqrt(n)>=allprimes[i]:
        if n%allprimes[i]==0:
            return False
        i+=1
    return True

def spiral_primes():
    num = 0
    denom = 1
    n = 1
    for i in range(1,30000):
        for j in range(4):
            n+=2*i
            if isprime(n):
                num +=1
            denom +=1
        if num/denom < 0.1:
            return i*2+1

print(spiral_primes())
    
