import json as json
import numpy as np
from matplotlib import pyplot as plt
import math
import itertools

### Problem statement at this link: https://projecteuler.net/problem=68


def perfect_5gon():
    lst = []
    outers = itertools.permutations([10,9,8,7,6])
    inners = itertools.permutations([5,4,3,2,1])
    for outer in outers:
        for inner in inners:
            ind = outer.index(6)
            val = outer[0]+inner[0]+inner[1]
            b = True
            for i in range(0,5):
                if outer[(ind+i)%5]+inner[(ind+i)%5]+inner[(ind+i+1)%5] != val: b = False
            if b:
                s = ""
                for i in range(0,5):
                    s = s + str(outer[(ind+i)%5])+str(inner[(ind+i)%5])+str(inner[(ind+i+1)%5])
                lst.append(s)
    return lst

print(perfect_5gon())
