import json as json
import numpy as np
from matplotlib import pyplot as plt
import math
from decimal import *

### This was the hardest problem yet, and I think it will be the hardest for me for a while. This code is really messy, but I don't really care. I don't understand
### the decimal package and dont need to, so I just threw in Decimal() around every number for every calculation. Without knowing researching Diophantes equations or 
### Pell's equation, this would have been impossible, other than by testing things out (and the 2 previous problems were all about continued fractions). However,
### While I was entering in numbers on the calculator in google, one of the searches I found had the number I entered into the searchbar, and the link was a list of
### terms in the continued fraction for sqrt(244), which is also 2sqrt(61). The number I was doing calculations with was the result of my brute force function when n=61, 
### so I realized there must be some relationship between continuted fractions and finding the solution to the diophantes equation in question. However, what did not occur to me
### was that this relationship was the best way to go about it, as I was almost sure I could limit my brute force search enough to make the problem feasible. However, after
### realizing that the numbers were so huge that I would need to use extra precision, and that even with the 1000x increase in speed that I had given the algorithm, the 
### needed precision just took too much power to compute, so I looked online for a hint about the problem. The first sentence of the first result I clicked on mentioned 
### continuing fractions, and with that information, the pieces of the puzzle fit together in my head, and I started coding a new program.


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

