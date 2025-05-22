import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

### Problem statement at this link: https://projecteuler.net/problem=72

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
allprimes = soe(100000)

def isprime(n):
    i = 0
    if n == 1:
        return False
    while math.sqrt(n)>=allprimes[i]:
        if n%allprimes[i]==0:
            return False
        i+=1
    return True

def unique_prime_factors(n):
    arr = []
    num = n
    while True:
        for p in allprimes:
             if num%p==0:
                if p not in arr:
                    arr.append(p)
                num/=p
                break
        if isprime(num):
            if num not in arr:
                arr.append(num)
            break
        if num == 1:
            break
    return arr

def counting_fractions():
    sum = 0
    for i in range(2,1000001):
        if i%1000==0:print(i)
        factors = unique_prime_factors(i)
        s=i
        for p in factors:
            s*=(1-1/p)
        sum+=s
    return sum

print(unique_prime_factors(3))
print(counting_fractions())

