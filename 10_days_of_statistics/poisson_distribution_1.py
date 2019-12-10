from math import *
def poisson(lmd, k):
    return round(pow(lmd, k) * pow(e, -lmd) / factorial(k), 3)

print poisson(2.5, 5)
