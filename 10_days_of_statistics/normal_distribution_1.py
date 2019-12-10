from math import *
from decimal import*
getcontext().prec = 40

def erf(x):
    return 1 - 1 / (Decimal(1 + 0.0705230784 * x + 0.0422820123 * x**2 + 0.0092705272 * x**3 + 0.0001520143 * x**4 + 0.0002765672 * x**5 + 0.0000430638*x**6))**16

def normal_cdf(a, b, mu, sigma, r):
    if a >= 0 and b >= 0:   return round(Decimal(0.5) * (1 + erf((b - mu) / (sigma * sqrt(2)))) - Decimal(0.5) * (1 + erf((a - mu) / (sigma * sqrt(2)))), r)
    if a < 0 and b >= 0:    return round(Decimal(0.5) * (1 + erf((b - mu) / (sigma * sqrt(2)))) - 1 + Decimal(0.5) * (1 + erf((-a + mu) / (sigma * sqrt(2)))), r)
    if a < 0 and b < 0:     return round(- Decimal(0.5) * (1 + erf((-b + mu) / (sigma * sqrt(2)))) + Decimal(0.5) * (1 + erf((-a + mu) / (sigma * sqrt(2)))), r)

print normal_cdf(-10**10, 19.5, 20, 2, 3)
print normal_cdf(20, 22, 20, 2, 3)
