from math import erf, sqrt
def normal_cdf(x, mu, sigma):
    return (1 + erf((x - mu) / sqrt(2) / sigma)) / 2

print round(normal_cdf(1.96, 0, 1), 4)
