import json as json
import numpy as np
from matplotlib import pyplot as plt
import math
import csv

results = []

with open("PE82.txt") as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        reader2 = csv.reader(row, delimiter=',')
        for row2 in reader2:
            results.append([int(i) for i in row2])

results = np.array(results)
print(results)

def path_sum_3way():
    bu = np.zeros([80,80])
    bu[:,0] = results[:,0]
    for j in range(1,80):
        for i in range(0,80):
            minpath = bu[i,j-1]
            if i > 0 and minpath>bu[i-1,j]:
                minpath = bu[i-1,j]
            if i<79:
                k = 1
                while i+k<80 and sum(results[i+1:i+k+1,j])<minpath:
                    if sum(results[i+1:i+k+1,j]) + bu[i+k,j-1]<minpath:
                        minpath = sum(results[i+1:i+k+1,j]) + bu[i+k,j-1]
                    k+=1
            bu[i,j] = minpath + results[i,j]
    return min(bu[:,79])
print(path_sum_3way())
