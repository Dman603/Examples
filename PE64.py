import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

### Problem statement at this link: https://projecteuler.net/problem=64

def next(n1,n2,n3):
    nn3 = (n1-n2**2)/n3
    return [n1,abs(n2-math.floor((math.sqrt(n1)+n2)/(nn3))*nn3),nn3]

def odd_period_sqare_roots():
    cnt = 0
    for i in range(2,10001):
        per = []
        b = True
        n1 = i
        n2 = math.isqrt(i)
        n3 = 1
        if math.isqrt(i)!=math.sqrt(i):
            while b:
                per.append([n1,n2,n3])
                n1,n2,n3 = next(n1,n2,n3)
                if [n1,n2,n3] in per:
                    b = False
                    if len(per[per.index([n1,n2,n3]):])%2==1:
                        cnt+=1
    return cnt

print(odd_period_sqare_roots())
