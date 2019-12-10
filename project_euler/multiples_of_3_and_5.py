def gauss_sum(n):
    return n * (n + 1) / 2

def foo(n):
    r = []
    start = n - 1
    while start % 3:
        start -= 1
    r.append(start / 3)
    start = n - 1
    while start % 5:
        start -= 1
    r.append(start / 5)
    r.append(r[0] / 5)
    s = 3 * gauss_sum(r[0]) + 5 * gauss_sum(r[1]) - 15 * gauss_sum(r[2])
    return s

#print foo(10**10)

def comparison(n):
    c = 0
    for _ in range(3, n):
        if not _ % 3 or not _ % 5: c += _
    return c

#for _ in range(1, 10001):
#    foo(10**_)

print foo(87)

print

print comparison(87)
