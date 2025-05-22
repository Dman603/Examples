import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

### I think there are a couple more tricks to speed this up, but this works pretty quickly. With each primitive the number of
### cuboids increases regularly as you change the factor of k. For example for 3,4,5 the number of cuboids is 3, and this
### increases linearly for 6,8,10 and 9,12,15 etc. If we were trying to do this for arbitrarily large cubes this would be
### the first change I would try to make to speed up the system.

### Anyway, the main idea of this problem is to see that you can treat the cubes as a net. You have 3 dimensions of the cube,
### i, j, k and therefore there are 3 different faces on the cube, and nCr(3,2)=3 ways to pick 2 faces on the cube. Basically you
### need to traverse 2 faces to get to the diagonal corner of the cube, and the way to find the minimal path of this is actually 
### pretty trivial when you draw a net of the cube. When you do this, you end up with a rectangle with dimensions i by (j+k)
### ( or j by (i+k) or k by (i+j) ). This is where we can remove the symmetrical solutions from the problem, by picking 
### to just focus on i by (j+k) and just asserting that i>=j>=k. Since the rectangle we are dealing with is i by (j+k) the 
### distance from corner to corner (from point S to point F) will be sqrt(i^2 + (j+k)^2) and this does in fact minimize distance.
### you can check this by trying to swap i and j or i and k and seeing that the resulting distance will be greater because we
### just asserted that i>=j>=k. This means that we now know how to find the minimal distance for any cuboid, but not we need
### to figure out which ones are integers. This also is pretty simple at its core, as basically the i by (j+k) rectangle 
### we just drew just has to be a pythagorean triple. In fact, at the core if this problem you dont even have to iterate through
### dimensions of the cuboid at all! It's actually very elegant, but it becomes very gross later on for other reasons which
### honestly I think are very cool. Basically, we can just generate pythagorean triples, and simply thefact that one exists
### while having certain properties about its side lengths is enough to know that a cuboid with one of these integer length
### distances exists as well.

### Basically, you have to generate primitive right triangles using euclids formula, picking an m, and an n which is coprime to n
### and basically iterating through all the coprime n until both sides of our triangle (a = m^2 - n^2, b = 2mn) are greater than
### the upper bound we set (this upper bound would be 100 for example in the case of the written problem statement). There
### are some complications with this that make us have to keep iterating through n until either a and b are 2 times the upper bound
### but only doing computations on the ones in which one of a or b is less than or equal to 100. One of a or b has to be less
### than or equal to 100 because the one of the side lengths will have to correspond to the side i of the cube, which is the
### longest side. The reason why we have to iterate until a and b are 2 times the upper bound though is because sometimes
### m^2 - n^2 and 2mn will both be greater than 100, but at a later n one of them will be less than 100. This got me stuck for a
### bit as the triangle 95, 168, ... has m = 12 and n = 7, but the previous coprime n was n = 5 and in this case where 
### m = 12 and n = 5 the triangle was 119, 120, ... which was causing my program to break before ever reaching n = 7. This
### behavior basically arises because m^2 - n^2 decreases with increasing n while 2mn increases. After I fixed this I got the
### correct solution.

### However, there is some more nuance to the problem, as for each pythagorean triple, there are multiple possible cuboids.
### Lets just look at an example. For the triangle 3,4,5 we actually have a couple of ways to make cuboids. The first is
### by letting i = 4. In this case (j+k) = 3 so we have the possible cuboid 4,2,1 but not 4,1,2 because that is symmetric
### by rotation ( ie 2 + 1 for j + k works but not 1 + 2). The other way we can orient the cuboid is with i = 3, and j + k = 4
### in this case we 3,3,1 AND 3,2,2 so we have j+k = 3+1 and 2+2. BOTH of these choises of i are valid AND UNIQUE cuboids, and
### therefore there are a total of 3 possible cuboids from the 3,4,5 triple (4,2,1  3,3,1  3,2,2). I came up with 2 formulas
### to determine the number of permutations, the first is cnt += b//2 and the second is cnt += b - ceil(a/2) + 1. This is when
### a>b, when b>a, a and b are swapped in the equations. Additionally, if either b or a is greater than the upper bound, it
### cannot take the place of the side length i on the cuboid, as that would mean the cuboid would have a side length greater
### than the upper bound we set for it. This means that only the cnt += b - ceil(a/2) + 1   (or cnt += a - ceil(b/2) + 1 if b>a)
### would be done in this case. To solve the problem you basically just have to iterate through m based on the bounds, and apply
### these equations fittingly depending on the values of a and b to add to the tally of cuboids. Additionally you have to 
### do non-primitive triples which you can just iterate through by multiplying a and b by a factor of k until a and be are
### greater than the bound. I really enjoyed how tangible this problem was and how it was complicated without requiring
### math that was too crazy. Done in 2 or 3 nights of work, ~10 hours.


def soe(n):
    arr = []
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n+1):
        if prime[p]:
            arr.append(p)
    return arr
# need primes to find numbers that are coprime
allprimes = soe(1000000)

def isprime(n):
    i = 0
    if n == 1:
        return False
    while math.sqrt(n)>=allprimes[i]:
        if n%allprimes[i]==0:
            return False
        i+=1
    return True
# need to tell if numbers are prime for coprime function


def coprime_n(n):
    num = n
    arr = np.array([True for k in range(num)])
    k = math.ceil(math.sqrt(num))+1
    i = 0
    while allprimes[i] < k:
        p = allprimes[i]
        if num%p==0:
            arr[::p]=False
            while num%p==0:
                num/=p
            k = math.ceil(math.sqrt(num))+1
            if isprime(num):
                arr[::int(num)]=False
                break
        i+=1
    return arr
# finds if numbers are coprime. Basically just tests prime factors of a number n up to sqrt(n)


def CuboidRoute():
    cnt = 0 # number of cuboids with integer length minimal paths from S to F
    bnd = 1818 # You have to change the bound manually until you find an output greater than 1,000,000
    for m in range(2,1000):
        idk = coprime_n(m)  # returns a boolean array of length m denoting what numbers are coprime based on index (its reversed for some reason)
        if m%2==0:
            cop = [i for i in range(len(idk[:(m+1)])) if (idk[i] and i!=0)] # converts the boolean array to a list of the coprime numbers
        else:
            cop = [i for i in range(len(idk[:(m+1)])) if (idk[i] and i!=0 and i%2==0)] # converts the same array to a list of coprime numbers except removint the ones that are even (one of m or n has to be even for euclids formula to work)
        for n in cop:
            if (m**2 - n**2)>2*bnd or (2*m*n)>2*bnd: break  # bound explained in heading
            if (m**2 - n**2)<=bnd or (2*m*n)<=bnd: # also explained in heading
                # legs of pythagorean triple
                a = m**2 - n**2
                b = 2*m*n
                # case where a>b as both a and b can be the largest depending on m and n.
                if a>b:
                    if a<=bnd:  # runs on triangles where both a and b are less than the bound, would not run on 85,132,157 for bnd = 100
                        cnt += b//2
                    cnt += max(0, b - math.ceil(a/2)+1) # runs all the time returns a value for a triangle like 85,132,157 for bnd = 100
                if b>a:
                    if b<=bnd:
                        cnt += a//2
                    cnt += max(0, a - math.ceil(b//2)+1)
                k = 2
                while k*(m**2 - n**2)<=bnd or k*2*m*n<=bnd: # I dont have to do the same weird bound thing because both a and b are increasing with k as in the last case a was creasing with n while b increased. 
                    a = k*(m**2 - n**2)
                    b = k*(2*m*n)
                    if a>b:
                        if a<=bnd:  
                            cnt += b//2
                        cnt += max(0, b - math.ceil(a/2)+1)
                    if b>a:
                        if b<=bnd:  
                            cnt += a//2
                        cnt += max(0, a - math.ceil(b//2)+1)
                    k+=1

    return cnt


print(CuboidRoute())