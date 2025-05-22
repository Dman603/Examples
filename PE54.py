import json as json
import numpy as np
from matplotlib import pyplot as plt
import math
import csv
results = []
with open("PE54_poker.txt") as csvfile:
    reader = csv.reader(csvfile, delimiter=' ') # change contents to floats
    for row in reader: # each row is a list
        results.append([row[0:5],row[5:10]])





def royal_flush(p1,p2):
    suits = ['D','C','H','S']
    winner = 0
    for i in range(len(suits)):
        if sorted(p1) == sorted(['10'+suits[i],'J'+suits[i],'K'+suits[i],'Q'+suits[i],'A'+suits[i]]):
            winner += 1
            
        if sorted(p2) == sorted(['10'+suits[i],'J'+suits[i],'K'+suits[i],'Q'+suits[i],'A'+suits[i]]):
            winner += -1
    return winner

def straight_flush(p1,p2):
    suits = ['D','C','H','S']
    order = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    winner = 0
    for i in range(len(suits)):
        for j in range(9):
            if sorted([c[:len(c)-1] for c in p1]) == order[j:5+j]:
                winner += 1
            if sorted([c[:len(c)-1] for c in p2]) == order[j:5+j]:
                winner += -1
    return winner

def four_of_a_kind(p1,p2):
    order = ['','2','3','4','5','6','7','8','9','T','J','Q','K','A']
    p1c = ''
    p2c = ''
    for o in order[1:]:
        cnt = 0
        for c in p1:
            if c[:-1]==o: cnt+=1
        if cnt == 4:
            p1c = o

    for o in order[1:]:
        cnt = 0
        for c in p2:
            if c[:-1]==o: cnt+=1
        if cnt == 4:
            p2c = o
    
    if order.index(p1c)>order.index(p2c):
        return 1
    elif order.index(p1c)<order.index(p2c):
        return -1
    else: return 0

def full_house(p1,p2):
    order = ['','2','3','4','5','6','7','8','9','T','J','Q','K','A']
    p1ps = ['','']
    p2ps = ['','']

    for o in order[1:]:
        cnt = 0
        for c in p1:
            if c[:-1]==o: cnt+=1
        if cnt == 3:
            p1ps[0] = o
        if cnt == 2:
            p1ps[1] = o

    for o in order[1:]:
        cnt = 0
        for c in p2:
            if c[:-1]==o: cnt+=1
        if cnt == 3:
            p2ps[0] = o
        if cnt == 2:
            p2ps[1] = o
    if '' in p1ps and '' in p2ps:
        return 0
    if '' in p1ps:
        return -1
    if '' in p2ps:
        return 1
    if '' not in p1ps and '' not in p2ps:
        if order.index(p1ps[0])>order.index(p2ps[0]):
            return 1
        elif order.index(p1ps[0])<order.index(p2ps[0]):
            return -1
        else: return 0
    else:
        return 0

def flush(p1,p2):
    suits = ['D','C','H','S']
    winner = 0
    for suit in suits:
        if [c[len(c)-1] for c in p1] == [suit for i in range(5)]:
            winner += 1
    for suit in suits:
        if [c[len(c)-1] for c in p2] == [suit for i in range(5)]:
            winner += -1
    return winner

def straight(p1,p2):
    order = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    winner = 0
    # subset shit is fucked since it doesnt count for order
    for i in range(9):
        if sorted([c[:len(c)-1] for c in p1]) == sorted(order[i:5+i]):
            winner += 1
        if sorted([c[:len(c)-1] for c in p2]) == sorted(order[i:5+i]):
            winner += -1
    return winner

def three_of_a_kind(p1,p2):
    order = ['','2','3','4','5','6','7','8','9','T','J','Q','K','A']
    p1c = ''
    p2c = ''
    for o in order[1:]:
        cnt = 0
        for c in p1:
            if c[:-1]==o: cnt+=1
        if cnt == 3:
            p1c = o

    for o in order[1:]:
        cnt = 0
        for c in p2:
            if c[:-1]==o: cnt+=1
        if cnt == 3:
            p2c = o
    
    if order.index(p1c)>order.index(p2c):
        return 1
    elif order.index(p1c)<order.index(p2c):
        return -1
    else: return 0

def two_pair(p1,p2):
    order = ['','2','3','4','5','6','7','8','9','T','J','Q','K','A']
    p1ps = ['','']
    p2ps = ['','']

    for o in order[1:]:
        cnt = 0
        for c in p1:
            if c[:-1]==o: cnt+=1
        if cnt == 2 and p1ps[0] == '':
            p1ps[0] = o
        elif cnt == 2 and p1ps[0]!='':
            p1ps[1] = o

    for o in order[1:]:
        cnt = 0
        for c in p2:
            if c[:-1]==o: cnt+=1
        if cnt == 2 and p2ps[0]=='':
            p2ps[0] = o
        elif cnt == 2 and p2ps[0]!='':
            p2ps[1] = o
    
    if '' in p1ps and '' in p2ps:
        return 0
    elif '' in p1ps:
        return -1
    elif '' in p2ps:
        return 1
    p1ps = [order.index(p1ps[0]), order.index(p1ps[1])]
    p2ps = [order.index(p2ps[0]), order.index(p2ps[1])]
    if max(p1ps)> max(p2ps):
        return 1
    if max(p1ps) < max(p2ps):
        return -1
    if min(p1ps) > min(p2ps):
        return 1
    if min(p1ps) < min(p2ps):
        return -1
    return 0

def pair(p1,p2):
    order = ['','2','3','4','5','6','7','8','9','T','J','Q','K','A']
    p1c = ''
    p2c = ''
    for o in order[1:]:
        cnt = 0
        for c in p1:
            if c[:-1]==o: cnt+=1
        if cnt == 2:
            p1c = o

    for o in order[1:]:
        cnt = 0
        for c in p2:
            if c[:-1]==o: cnt+=1
        if cnt == 2:
            p2c = o
    
    if order.index(p1c)>order.index(p2c):
        return 1
    elif order.index(p1c)<order.index(p2c):
        return -1
    else: return 0

def high_card(p1,p2):
    order = ['','2','3','4','5','6','7','8','9','T','J','Q','K','A']
    p1arr = sorted([order.index(c[:len(c)-1]) for c in p1])[::-1]
    p2arr = sorted([order.index(c[:len(c)-1]) for c in p2])[::-1]
    for i in range(5):
        if p1arr[i]>p2arr[i]:
            return 1
        elif p1arr[i]<p2arr[i]:
            return -1
    return 0

def poker_hands():
    score = 0
    for res in results[:]:
        cnt = [royal_flush(res[0],res[1]),straight_flush(res[0],res[1]),four_of_a_kind(res[0],res[1]),full_house(res[0],res[1]),flush(res[0],res[1]),straight(res[0],res[1]),three_of_a_kind(res[0],res[1]),two_pair(res[0],res[1]),pair(res[0],res[1]),high_card(res[0],res[1])]
        for item in cnt:
            if item == -1:
                break
            if item == 1:
                score+=1
                break
    return score


print(poker_hands())


            




    


