import json as json
import numpy as np
from matplotlib import pyplot as plt
import math
import csv

### Problem statement at this link: https://projecteuler.net/problem=81

results = []

with open("PE81.txt") as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        reader2 = csv.reader(row, delimiter=',')
        for row2 in reader2:
            results.append([int(i) for i in row2])

results = np.array(results)
print(results)

def path_sum_2way():
    bu = np.zeros([80,80])
    bu[0,0] = results[0][0]
    for i in range(1,159):
        for j in range(0,-abs(i-79)+80):
            #pos = [i-j,j]
            if i<80:
                if i-j == 0:
                    bu[i-j,j] = bu[i-j,j-1] + results[i-j,j]
                elif j == 0:
                    bu[i-j,j] = bu[i-j-1,j] + results[i-j,j]
                else:
                    print(results[i-j][j]+min(bu[i-j-1,j], bu[i-j,j-1]))
                    bu[i-j,j] = (results[i-j][j]+min(bu[i-j-1,j], bu[i-j,j-1]))
            else:
                print(results[i%80 + j+1][79-j]+min(bu[i%80 + j,79-j], bu[i%80 + j,79-j-1]))
                bu[i%80+j+1,79-j] = (results[i%80 + j+1][79-j]+min(bu[i%80 + j,79-j], bu[i%80 + j +1,79-j-1]))
    return bu

print(path_sum_2way()[71:,71:])
print(results[71:,71:])
