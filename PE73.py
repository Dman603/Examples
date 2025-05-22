import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

### Problem statement at this link: https://projecteuler.net/problem=73

### I think there is a much more elegant solution that has to do with just dividing the distance between the upper and lower bounds by each of the factors, however with multiple
### factors this leads to double counts, so you would have to do nCr(np,2) divisions where np is the number of prime factors. However, np is never more than 6, since 
### 2*3*5*7*9*11*13 > 12000


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
allprimes = soe(20000)

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
    for i in range(4,12001):
        if i%1000==0:print(i)
        factors = unique_prime_factors(i)
        lb = math.floor(i/3)+1
        ub = math.ceil(i/2)
        for j in range(lb,ub):
            bl = True
            for p in factors:
                if j%p==0:
                    bl = False
                    break
            if bl:
                sum+=1

    return sum

print(counting_fractions())
