import math

### Problem statement at this link: https://projecteuler.net/problem=63

def powerful_digit_counts():
    return sum([math.floor(1/(1-math.log10(i))) for i in range(1,10)])

print(powerful_digit_counts())
