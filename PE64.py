import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

### It's unfortunate that floating point error exists (and that it starts fucking up after only 8 decimal places!?) as it makes it nearly impossible to implement the most elegant
### solution to this, which allows you to ignore any terms, and just use calculated floats, iterating to the next number where n = (1/n)%1 and appending this result to a set.
### for the larger numbers like 9999 I think this literally does not work due to floating point error, as for numbers that large there may in fact be values that are within the
### same magnitude of 10^-7. Plus, having to round like 3 times for each number slows everything down a lot more than expected. Maybe just using precision doubles would help
### but honestly this runs pretty fast, and its exactly the thing that the number one post of the forums did.

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
