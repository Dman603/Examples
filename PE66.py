import json as json
import numpy as np
from matplotlib import pyplot as plt
import math
from decimal import *

### Problem statement at this link: https://projecteuler.net/problem=66

### This was the hardest problem yet, and I think it will be the hardest for me for a while. Without knowing researching Diophantes equations or 
### Pell's equation, this would have been impossible, other than by testing things out (and the 2 previous problems were all about continued fractions).


getcontext().prec = 200

def convergents_of_sqrtn(n):
    num = Decimal(n)
    val = Decimal(1)/(num.sqrt()%1)
    numers = [math.isqrt(n),1]
    for i in range(1,1000):
        mul = math.floor(Decimal(val))
        nnum = numers[0]*mul + numers[1]
        b = Decimal(( (( Decimal(nnum)**Decimal(2) - Decimal(1) ) / Decimal(n)) ))
        if math.floor(b)==b: return nnum
        numers[1] = numers[0]
        numers[0] = nnum
        val = Decimal(1)/(Decimal(val)%Decimal(1))



def diophantes_equation():
    largestx = 0
    maxd = 0
    for i in range(1,1000):
        if math.sqrt(i)!=math.isqrt(i):
            plc = convergents_of_sqrtn(i)
            if plc > largestx:
                largestx = plc
                maxd = i

    return largestx, maxd

print(diophantes_equation())

