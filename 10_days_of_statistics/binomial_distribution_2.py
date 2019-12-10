def binomial_coefficient(n, k):
    num, d = 1, 1
    for _ in range(k):
        num *= (n - _)
        d *= (_ + 1)
    return num / d

def binomial_distribution(n, k, p):
    return binomial_coefficient(n, k) * p**k * (1 - p)**(n - k)

def binomial_cumulative(n, k, p):
    P = 0
    for _ in range(k + 1):
        P += binomial_distribution(n, _, p)
    return round(P, 3)

print binomial_cumulative(10, 2, 0.12)
print 1 - binomial_cumulative(10, 1, 0.12)
