from math import factorial
def d_f (n):
    s = 0
    for _ in xrange(10, n):
        tmp =  sum(map(factorial, map(int, str(_))))
        if tmp % _ == 0: s += _
    return s

print d_f(20)
