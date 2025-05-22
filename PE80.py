import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

### Problem statement at this link: https://projecteuler.net/problem=80

def func(x):
    if x<50: return 0
    else: return x-50

def square(a):
    inp = np.array(a)
    out = np.convolve(inp,inp)
    carryover = 0
    for i in range(np.size(out)-1,-1,-1):
        temp = out[i] + carryover
        out[i] = (temp) % 10
        carryover = temp//10
    out[0]=out[0] +carryover*10
    return out[:]

def sqrt_dig_expansion():
    lb = 1
    s = 0
    for n in range(2,101):
        if n**0.5 == int(n**0.5):
            lb+=1
            print(n)
        else:
            arr = [lb]
            for i in range(100):
                for k in range(1,10):
                    if square(arr +[k])[0]>=n:
                        arr = arr + [k-1]
                        break
                else:
                    arr = arr + [k]
            print(arr)
            s += sum(arr[:-1])
    return s
print(sqrt_dig_expansion())
print(10**0.5)



