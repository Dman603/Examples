import json as json
import numpy as np
from matplotlib import pyplot as plt
import math



def counting_summations():
    arr = np.zeros([100,100])
    for i in range(0,100):
        arr[i,i] = 1
        for j in range(0,math.ceil((i)/2)):
            arr[i,j] += sum(arr[i-j-1,j:])
    return arr


print(counting_summations()[:14,:14])
