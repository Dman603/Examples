import json as json
import numpy as np
from matplotlib import pyplot as plt
import math
import csv

### Problem statement at this link: https://projecteuler.net/problem=67

results = []

with open("PE67_triangle.txt") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        reader2 = csv.reader(row, delimiter=' ')
        for row2 in reader2:
            results.append([int(i) for i in row2])

def maximum_path_sum_2():
    vals = results[len(results)-1]
    bu = []
    for i in range(98,0,-1):
        for j in range(len(results[i])-1):
            print(bu)
            bu.append(results[i][j]+max(vals[j],vals[j+1]))
        vals = bu
        bu = []
    return vals[0]+59

print(maximum_path_sum_2())
