import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

### Problem statement at this link: https://projecteuler.net/problem=60

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

sieveprimes = [p for p in allprimes if p!=2 and p!=5]


def prime_pair_sets(n):
    mseed = [[sieveprimes[i]] for i in range(n)]
    pairs = [mseed, [], [], [], []]
    for j in range(4):
        for item in pairs[j]:
            for i in range(sieveprimes.index(item[j]),sieveprimes.index(item[j])+1000):
                b = True
                for num in item:
                    if ( not isprime(sieveprimes[i]*10**math.ceil(math.log10(num))+num)) or (not isprime(num*10**math.ceil(math.log10(sieveprimes[i]))+sieveprimes[i])):
                        b = False
                        break
                if b:
                    arr = [plc for plc in item]
                    arr.append(sieveprimes[i])
                    (pairs[j+1]).append(arr)
                if sum(item) + sieveprimes[i] > 30000:
                    break
        print(pairs[j+1])
    
    return pairs[4]

print(prime_pair_sets(5))








