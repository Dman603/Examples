import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

### This is boring. I didn't do any other project euler problem for literally over a year
### because of this dogshit problem. This isn't even hard. Literally all you have to do is
### read the wikipedia article for partitions, and the answer ends up being right there.
### All the work I put into making creative solutions didn't matter, and when I finally
### decided to search into the problem a year later, it just dumbed down the problem too 
### much. It would have been nice if the first one that was divisible by a million was not
### in the 50000's. If it was like in the early millions, it would have been a much more
### fun experience solving the problem. Once thing I realized about the problem to speed 
### it up (uselessly because the solution appears so early) was that you can ignore any 
### digits in all of the numbers that are large than the millions place. This is because
### of the additive way that the recursion works. Since we only want to know which number
### mod 1000000 == 0, all the other digits dont matter for our answer, and because finding
### each term requires adding terms prior, it makes no difference whether we ignore all those
### larger digits as the ten-millions place will never impact the millions place (however
### the vice versa does not apply, as carryover from adding millions will impact the
### ten-millions place). This means that we do not have to store thousands of numbers with
### hundreds of digits, and only have to save 6 of the digits. This saves a lot of memory
### as the numbers get larger. This would have been useful if the problem was harder, but
### the solution is very early on so it really only speeds up the problem a slight amount.
### This was a shame of a problem to work on, and only hindered my growth as a programmer
### as the optimization to solve the problem is near impossible to come up with, and is
### just rather bizarre. I need to set myself a time limit on these things. This 25%
### difficulty problem didnt even end up being that difficult, so it's really not like
### any of these problems are an issue of me being too dumb. If I spend 100 hours on a
### problem, I need to google something.

def coin_partitions():
    arr = np.array([1,1])
    pent = ([(3*k**2-k)//2 for k in range(-2000,2000)])
    pent.sort()
    for i in range(2,2000000):
        if i%10000==0: print(i)
        su = 0
        k = 1
        while pent[k] <= i:
            if k%4 == 1 or k%4 == 2:
                su = su + arr[i-pent[k]]
            else: su = su - arr[i-pent[k]]
            k+=1
        n = su%1000000
        if(n==0): return "THIS IS THE NUMBER:" + str(i)
        arr = np.append(arr,n)
    return arr[1990000:2000000]

print(coin_partitions())
