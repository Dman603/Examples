import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

### Problem statement at this link: https://projecteuler.net/problem=51

### Didn't try to find a good way to actually check which of the numbers the code spits out is the least. Really the question is kinda vague in not saying if a number like 
### 000109 would count as being lower, as it is technically part of the same family. Either way there were only 4 possible answers, and its pretty clear which one 
### is probably considered to be the least just by looking at it


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
print(len(allprimes))

def isprime(n):
    i = 0
    if n == 1:
        return False
    while math.sqrt(n)>=allprimes[i]:
        if n%allprimes[i]==0:
            return False
        i+=1
    return True

def cycle_perm(p, max):
    perm = p
    perm[len(perm)-1]+=1
    for pos in range(1,len(perm)+1):
        if perm[len(perm)-pos] == max-pos+2:
            perm[len(perm)-pos-1] +=1
            perm[len(perm)-pos] = perm[len(perm)-pos-1]+1
            for f in range(len(perm)-pos+1,len(perm)):
                perm[f] = perm[len(perm)-pos]+f-len(perm)+pos
    return perm


def prime_digit_replacements():
    arr = []
    for l in range(5,7):
        for g in range(3,l,3):
            perm = [k for k in range(g)]
            for p in range((math.factorial(l-1)//(math.factorial(g)*math.factorial(l-1-g)))):
                num = [0 for plc in range(l)]
                for i in range(10**(l-g)):
                    score = 0
                    for k in range(0,10):
                        cnt = (l-g)
                        st = ""
                        for base in range(l):
                            if base in perm:
                                num[base] = k
                            else:
                                num[base] = (i%(10**cnt))//(10**(cnt-1))
                                cnt = cnt-1
                        
                        for buff in range(l):
                            st+=str(num[buff])
                        if isprime(int(st)):
                            score+=1
                        if score == 8: arr.append([st,i])


                perm = cycle_perm(perm, l-2)
    return arr

print(prime_digit_replacements())
                            


                
