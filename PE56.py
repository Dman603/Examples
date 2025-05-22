import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

### Not really sure how good this approach is. I know that it would be a lot faster to just let python manage the large numbers
### but I feel like that would go against the point of the problem, as coming up with a novel approach to deal with numbers
### on the scale of 10^200 is part of the challenge that the problem would have presented when it was released in 2005 or so


def powerful_digit_sum():
    mdigsum = 0
    ij = []
    for i in range(11,100):
        n = [0 for plc in range(200)]
        n[0] = i%10
        n[1] = i//10
        for j in range(1,100):
            n = [plc * i for plc in n]
            su = 0
            for k in range(198):
                n[k+2] += (n[k]%1000)//100
                n[k+1] += (n[k]%100)//10
                n[k] = n[k]%10
            if sum(n)>mdigsum:
                ij= [i,j]
                mdigsum = sum(n)
    return mdigsum, ij
            
                
    

print(powerful_digit_sum())