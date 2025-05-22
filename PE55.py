import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

def lychrel_numbers():
    score = 0
    for i in range(1,10000):
        n = i + int(str(i)[::-1])
        cnt = 0
        while n != int(str(n)[::-1]) and cnt<=50:
            n = n + int(str(n)[::-1])
            cnt+=1
        if cnt >=50:
            score+=1
    return score

print(lychrel_numbers())