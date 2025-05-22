import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

def convergents_of_e():
    numers = [3,2]
    for i in range(3,101):
        if i%3==0: mul = (i//3)*2
        else: mul = 1
        nnum = numers[0]*mul + numers[1]
        print(nnum)
        numers[1] = numers[0]
        numers[0] = nnum
    return sum([int(ch) for ch in str(numers[0])]), numers

print(convergents_of_e())
        
