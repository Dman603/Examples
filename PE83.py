import json as json
import numpy as np
from matplotlib import pyplot as plt
import math
import csv

### Problem statement at this link: https://projecteuler.net/problem=83

size = 80
results = []

with open("PE82.txt") as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        reader2 = csv.reader(row, delimiter=',')
        for row2 in reader2:
            results.append([int(i) for i in row2])

results = np.array(results)

#results = np.array([[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]])
print(results)

bu = np.zeros([size,size])
bu[0,0] = results[0,0]
ub = 1
def path_sum_4way():
    for i in range(1,size*2 - 1):
        print(i)
        ubmin = 10000
        for j in range(0,-abs(i-size+1)+size):
            global ub
            ub = ubmin +10000
            if i < size:
                bu[i-j,j] = branch([[i-j,j]],0)
                if bu[i-j,j] < ubmin: ubmin=bu[i-j,j]
            else:
                bu[i%size + j+1,size-1-j] = branch([[i%size + j+1,size-1-j]],0)
                if bu[i%size + j+1,size-1-j] < ubmin: ubmin=bu[i%size + j+1,size-1-j]
    return bu

def branch(pos,sum):
    c = pos[-1]
    global ub
    if bu[c[0],c[1]] != 0:
        if sum + bu[c[0],c[1]] < ub:
            ub = sum + bu[c[0],c[1]]
        return bu[c[0],c[1]] + sum
    sum += results[c[0],c[1]]
    if sum>=ub or bu[c[0],c[1]] >=10e9 or len([str(item) for item in pos]) != len(set([str(item) for item in pos])):
        return 10e9
    arr = []
    if c[0] != 0: arr += [branch(pos + [[c[0] - 1, c[1]]], sum)]
    if c[0] != size-1: arr += [branch(pos + [[c[0] + 1, c[1]]], sum)]
    if c[1] != 0: arr += [branch(pos + [[c[0], c[1] - 1]], sum)]
    if c[1] != size-1: arr += [branch(pos + [[c[0], c[1] + 1]], sum)]
    #print(arr)
    return min(arr)

#print(branch([[0,4]],0,2000))
print(path_sum_4way())

