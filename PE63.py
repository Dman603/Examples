### Solved on the toilet with desmos: ceil(log(x)) = log_b(x) and just count the lines. There is a better way to do it by measuring the fator between 1 and log(b) and seeing
### how many times you need to multiply that to get 1

import math

def powerful_digit_counts():
    return sum([math.floor(1/(1-math.log10(i))) for i in range(1,10)])

print(powerful_digit_counts())