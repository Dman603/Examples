import json as json
import numpy as np
from matplotlib import pyplot as plt
import math
import csv

### Problem statement at this link: https://projecteuler.net/problem=59


with open("PE59_cipher.txt") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        results = row

results = [int(item) for item in results]

def xor_decryption():
    key = [[],[],[]]
    for c in key:
        for i in range(97,123):
            b = True
            decr = [item^i for item in results[key.index(c)::3]]
            for item in decr:
                if (item!=32 and (item<32 or item>122)) or item==96:
                    b = False
            if b:
                c.append(i)
    s = ""
    for item in (list((np.ravel([[chr(k^key[results[i*3:i*3+3].index(k)][0]) for k in results[i*3:i*3+3]] for i in range(len(results[::3]))])))):
        s+= item
    return s

s = 'An extract taken from the introduction of one of Euler\'s most celebrated papers, "De summis serierum reciprocarum" [On the sums of series of reciprocals]: I have recently found, quite unexpectedly, an elegant expression for the entire sum of this series 1 + 1/4 + 1/9 + 1/16 + etc., which depends on the quadrature of the circle, so that if the true sum of this series is obtained, from it at once the quadrature of the circle follows. Namely, I have found that the sum of this series is a sixth part of the square of the perimeter of the circle whose diameter is 1; or by putting the sum of this series equal to s, it has the ratio sqrt(6) multiplied by s to 1 of the perimeter to the diameter. I will soon show that the sum of this series to be approximately 1.644934066842264364; and from multiplying this number by six, and then taking the square root, the number 3.141592653589793238 is indeed produced, which expresses the perimeter of a circle whose diameter is 1. Following again the same steps by which I had arrived at this sum, I have discovered that the sum of the series 1 + 1/16 + 1/81 + 1/256 + 1/625 + etc. also depends on the quadrature of the circle. Namely, the sum of this multiplied by 90 gives the biquadrate (fourth power) of the circumference of the perimeter of a circle whose diameter is 1. And by similar reasoning I have likewise been able to determine the sums of the subsequent series in which the exponents are even numbers.'
su = 0
for ch in s:
    su+=ord(ch)
print(su)



#print(xor_decryption())
