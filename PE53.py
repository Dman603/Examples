import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

### This could probably be done by hand if I was actually good at math, but I really know nothing about the gamma function. The only thing that I can really do at this time is loop 
### Through all of the possible combinations.

### However, I do feel bad about solving the problem in this way, because once again this problem was released in like 2004, and it seems unfair to just abuse the ability to do 
### calulations with numbers as large as these in such an easy way with python now. I think a way that could make the numbers more managable though would be to wait until
### you hit a number that is greater than a million in each i cycle, then start a multiplier that will keep track of number from there. For the rest of the current i cycle
### each time j increments, you multiply the multiplier by (j+1)/(i-j) which is basically the ratio of consecutive nCr values as you increment r. When this multiplier falls
### back below 1, it will mark that the number is no longer greater than a million, and the counter should increment for each j from the creation of the multiplier to the
### point where it fell below 1, as all of those values are greater than a million. Even with this the numbers still might be too big though, so I guess you could start
### the multiplier as like 10^-6 or something like that but it doesnt really matter that much I dont think, really just writing this to work through the possiblities for 
### myself for learning purposes as I think spending the time to implement it wouldn't really help as much as just brainstorming ideas to be honest.

def combinatoric_selections():
    cnt = 0
    for i in range(1,101):
        for j in range(1,i):
            if math.comb(i,j) >= 10**6:
                cnt+=1
    return cnt

print(combinatoric_selections())

