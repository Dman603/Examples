import json as json
import numpy as np
from matplotlib import pyplot as plt
import math


### Problem statement at this link: https://projecteuler.net/problem=61


def what_is_this(arr, bigarr):
    why = [0,0,0,0,0,0]
    for item in arr[1:]:
        for l in range(1,6):
            if item in bigarr[l]: why[l]+=1
    b = True
    for c in why:
        print(why)
        if c>1: b = False
    return b

def cyclical_figurate_numbers():
    lists = [
        [(n**2+n)/2 for n in range(200) if (n**2+n)/2<10000 and (n**2+n)/2>=1000],
        [(n**2) for n in range(200) if n**2<10000 and n**2>=1000],
        [(3*n**2-n)/2 for n in range(200) if (3*n**2-n)/2<10000 and (3*n**2-n)/2>1000],
        [(2*n**2-n) for n in range(200) if (2*n**2-n)<10000 and (2*n**2-n)>=1000],
        [(5*n**2-3*n)/2 for n in range(200) if (5*n**2-3*n)/2<10000 and (5*n**2-3*n)/2>1000],
        [(3*n**2-2*n) for n in range(200) if (3*n**2-2*n)<10000 and (3*n**2-2*n)>=1000],
    ]
    idk = [[n] for n in lists[0]]
    for i in range(1,6):
        temp = []
        for j in range(len(idk[:][:-1])):
            for num in lists[1]+lists[2]+lists[3]+lists[4]+lists[5]:
                if idk[j][-1]%100==num//100:
                    temp.append(idk[j]+[num])
        idk = temp
        for item in idk:
            if len(item)!=i+1: idk.remove(item)
    return [sum(item[:]) for item in idk if item[-1]%100==item[0]//100 and what_is_this(item, lists)]


print(cyclical_figurate_numbers())
