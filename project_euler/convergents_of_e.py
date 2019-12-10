from fractions import Fraction
from math import log
def arr_continued_fraction(n):
    a = [1]
    tmp = 2
    for _ in xrange(1, n - 1): 
        if (_ - 1) % 3 == 0:
            a.append(tmp)
            tmp += 2
        else: a.append(1)
    return a[::-1]

def continued_fraction(arr):

    if len(arr) == 1: return Fraction(1, arr.pop())
    return Fraction(1, arr.pop() + continued_fraction(arr))

def foo(n):
    if n == 1: return 2
    return sum(map(int, str((2 + continued_fraction(arr_continued_fraction(n))).numerator)))


def continued_fraction_2nd_try(n):
    arr = arr_continued_fraction(n)
    if n == 1: return 2
    if n == 2: return 3
    s = (arr[1] + Fraction(1, arr[0]))**(-1)
    for _ in arr[2:]:   
        s += _
        s **= -1
    return sum(map(int, str((2 + s).numerator)))






def continued_fraction_3rd_try(n):
    arr = arr_continued_fraction(n)

    if n == 1: return 2
    if n == 2: return 3
    n, d = 1, arr[0]

    for _ in arr[1:]:   
        n, d = d, d * _ + n
#    return float(2 * d + n) / d, 2 * d + n, d, sum(map(int, str(2 * d + n))), int(log(2 * d + n, 10)) + 1

#    return 2 * d + n, d, sum(map(int, str(2 * d + n))), int(log(2 * d + n, 10)) + 1

#    return sum(map(int, str(2 * d + n))), int(log(2 * d + n, 10)) + 1

    return int(log(2 * d + n, 10)) + 1

print continued_fraction_3rd_try(10**6)
