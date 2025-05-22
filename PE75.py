import json as json
import numpy as np
from matplotlib import pyplot as plt
import math

### Problem statement at this link: https://projecteuler.net/problem=75

### I still want to see if there is a way to solve this with the other approach I was taking where you iterate through each length individually and use the 
### quadratic I found to compute a,b based on c,l
### The strategy does work, after testing it against the one that actually works Ive gotten the same values. The issue is it takes about 10000x longer. However
### I do think there is a way to iterate through it differently, as I believe you can specifically skip values based on how the quadratic is structured
### I believe for this there would be some sort of substitution into the radical, this would also remove a lot of the computation in each cycle as well, so I think there could be
### a decent factor of 1000 speed increase even.

### However, the approach that actually functions now is similar to the initial approach I took after a while, which was to find every single triangle using Euclid's formula. 
### All this does is give you a way to generate primitive right triangles by inputting certain integer values.
### Euclids formula takes two positive integers as input, m and n, where m>n, and m and n are coprime. If these conditions are not met, nonprimitive integer right triangles will
### be generated. The formula states a = m^2 - n^2, b = 2mn, c = m^2 + n^2. To apply this to my problem, I can begin with the fact that l = a + b + c, and just substitute these
### m and n values in. This gives us l = 2m^2 + 2mn, as some of the terms cancel. With this we learn the first interesting fact about this problem that lets us shave down time
### since m and n are both integers, l/2 has to be an integer, which can be seen when you divide both sides of the equation by 2. This is the first idea that can be applied,
### however, this problem is somewhat of a multivariable integration problem where you have to find the bounds based on different variables which you are going to iterate over.
### Using this logic, you can begin to deduce the bounds of this nested for loop. An obvious one is that m>n>0, which actually only partially defines the bound I used in this program
### the bounds for n are a little interesting, as although leaving it just at that; increasing n until it reaches m, would in fact work, for larger values of m, it becomes very 
### inefficient. This is where the equation I referenced last comes in. Since the maximum l = 1,500,000 we can set up an inequality of 750000 >= m^2 + mn. If we are trying
### to find the bounds of n, we can just rework the inquality to be in terms of n. This ends up as 750000/m - m = n. I basically just ignored the - m since this is the maximum
### bound and I think it would have just caused more trouble being called in the for loop for many of the smaller numbers actually causing a decrease in speed. Basically this
### bound is the maximum n can be for a given m so that the length does not surpass 1500000. This actually gives us a second constraint on n in addition to the m>n>0 bound
### basically the minimum of these two values is the one you want to use in each iteration to minimize the time spent. Since the formula has to follow both constraints, 
### it must always be lower than both of them, so this works. In fact you could technically just use one or the other and it would still work, just take much longer.
### the bounds for m are conceptually complicated in a certain way, as its basically the same thing you have to do for multivariate integration bounds. Basically there is a value
### of n which will maximize m, which needs to be substituted into the equation, which can then be solved in terms of m and only m. This value happens to be 1 (n cant be 0) but this
### can be analyzed analitically by taking the first partial derivitive of the equation with respect to m, which is 2m + n. if both m and n are positive, this means that the
### partial derivitive can only equal zero when both m and n are 0. However, this technically isnt possible since 0 isnt in the domain, so we have to check endpoints as well
### the endpoints for n are 1 and m - 1, so substituting these in we find that 1 is clearly the maximizing value for m. Substituting 1 in for n gives the expression
### 750000 >= m^2 + m. Now here we can either solve a quadratic, or just do sqrt(750000) which works because sqrt(750000 - m) would be lower, so its actually a 
### slight overestimate to do it this way. After this you can just iterate through all m based on these bounds, and generate a list of numbers coprime to m based on the bounds
### for n. Theres also something weird that needs to be done where both m and n cannot be odd, so for odd m you basically have to make sure to remove all odd numbers from the list
### of generated coprimes. Using all of this information can generate you a list of all primitive right triangles (and their lengths). Something interesting I found which was
### annoying while trying to work everything out was that there are some larger primitive triangles which have the same length of other primitive triangles. This made it hard to
### do the problem without masking when I was trying to do it a few months ago. Once you have a list of the lengths of all primitive right triangles, you basically need to create 
### a integer mask of each value from 0 to 1500000. This allows you to iterate through each length of primitive triangle and do the following computation on the mask:
### arr[::prim] += 1. This essentially is iterating the index of the mask corresponding to each multiple of the length of each triangle (for every primitive triangle,
### k*length is also the length of another right triangle which is not primitive). Basically this allows us to keep track of every possible length of triangle, and find 
### which ones are multiples of only one other primitive triangle (or are primitive themselves, 12%12==0 is true). A binary mask would have been possible for this if it wanted you
### to find all integer right triangles, but the fact that it did not want ones which had the same length as another made it so that you have to keep track of the multiplicity of this
### its not hard initially when you are just dealing with primitives, but there are also many nonprimitives which are only composed of a single primitive, and not two.
### this is the issue where you have to actually keep track of how many triangles an individual length is a multiple of.

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

def unique_prime_factors(n):
    factors = []
    num = n
    k = math.ceil(math.sqrt(num))+1
    i = 0
    while allprimes[i] < k:
        p = allprimes[i]
        if num%p==0:
            factors.append(p)
            while num//p == num/p:
                num/=p
            k = math.ceil(math.sqrt(num))+1
            if isprime(num):
                factors.append(int(num))
                return factors
        i+=1
    return factors
        

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


def check_duplicates(a):
    arr = a
    u = np.unique(a)
    d = np.array(a)
    lol = d[np.isin(d,u, invert = True)]
    return lol[:10]


        

def single_integer_right_triangles():
    total = 0
    for i in range(12,15000,2):

        kek = 0
        for j in range(math.ceil(i/(2.41421356237)),i//2):
            if ((2*i-2*j+math.sqrt(8*i*j+4*j*j-4*i*i))/4).is_integer():
                #print((2*i-2*j+math.sqrt(8*i*j+4*j*j-4*i*i))/4)
                kek+=1
        if kek == 1:
            print(i)
            total+=1
    return total

def kek():
    for i in range(12,1500000):
        if i%10000 == 0: print(i)
        coprime_n(i)
    return

def dogshitsqrt(l):
    for c in range(math.ceil(l/2.41421356237),l//2):
        if((2*l-2*c+math.sqrt(8*l*c+4*c*c-4*l*l))/4).is_integer():
            print((2*l-2*c-math.sqrt(8*l*c+4*c*c-4*l*l))/4,(2*l-2*c+math.sqrt(8*l*c+4*c*c-4*l*l))/4,c)


def all_prims():
    arr = []
    for m in range(2,math.ceil(math.sqrt(750000))):
        if m%100==0: print(m)
        idk = coprime_n(m)
        if m%2==0:
            cop = [i for i in range(len(idk[:(min(m,750000//m)+1)])) if (idk[i] and i!=0)]
        else:
            cop = [i for i in range(len(idk[:(min(m,750000//m)+1)])) if (idk[i] and i!=0 and i%2==0)]
        for n in cop:
            if m**2+m*n > 750000: break
            meh = 2*m**2+2*m*n
            arr.append(meh)
    return arr

def idfkanymore():
    total = 0
    arr = all_prims()
    mask = np.array([0 for i in range(1500001)])
    for prim in arr:
        mask[::prim]+=1
    for item in mask:
        if item==1: total+=1
    return total
print(idfkanymore())




