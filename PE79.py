import json as json
import numpy as np
from matplotlib import pyplot as plt
import math
import csv

### I have no idea what this problem even is, I just kinda guessed until
### I got it right, but I did use a certain approach to get a good starting
### value, then tweaked the answer until it worked in my test. I guess I could
### have eventually automated the adding of numbers into the answer, but
### it ended up being simple without it.

results = []

with open("PE79.txt") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        results += row
        
results = list(set([int(item) for item in results]))
print(results)

def passcode_derivation():
    out = np.zeros([10,3])
    for k in range(0,3):
        arr = np.array([(item//10**k)%10 for item in results])
        print(arr)
        for i in range(0,10):
            out[i,2-k] = np.size((np.where(arr==i)[0]))
    return out

out = passcode_derivation()
print(out)
out = 73162890

def test():
    idk = [int(item) for item in list(str(out))]
    print(idk)
    for item in results:
        temp = idk
        for digit in str(item):
            try: 
                temp = temp[temp.index(int(digit))+1:]
            except ValueError:
                print("you need to add" + str(digit) + " number:"  + str(item))
    return

test()
        


