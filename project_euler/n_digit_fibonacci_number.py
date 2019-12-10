from math import sqrt, log, ceil
def fibonacci(n):
    a, b = 0, 1
    count = 1
    while count < n:
        a, b = b, a + b

        count += 1
    return  b


""" Fib_n =  phi**n - psi**n / (phi - psi) """

phi = (1 + sqrt(5)) / 2
psi = (1 - sqrt(5)) / 2

def fib_digits_lower_bound(d):
    return int((d + 0.5 * log(5, 10) - 1) / log(phi, 10))
""" the minus one ensures that the returned value is a lower bound, since
    1 n*log(phi, 10) - 0.5 * log(5, 10) <= ceil(n*log(phi, 10) - 0.5 * log(5, 10))"""



def digits(n):
    return int(ceil(n*log(phi, 10) - 0.5 * log(5, 10)))


def digits_of_nth_fibonacci_number(d):
    start = fib_digits_lower_bound(d)
    while digits(start) < d:
        start += 1
    return start

print digits_of_nth_fibonacci_number(10**100)
print
#print digits(10**6)
print fibonacci(10**6)

def n_th_large_fib_golden_ratio(n):
    return phi**n / sqrt(5)

#print n_th_large_fib_golden_ratio(10**3)
