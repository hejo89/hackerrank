from math import sqrt

def prime(n, r, start):
    if n == 1: return r
#    if n == 1: return max(r)
    if n % 2 == 0:
        count = 1
        n /= 2
        while n % 2 == 0:
            n /= 2
            count += 1
        return prime(n, [2] * count, 3)
    for _ in xrange(start, int(sqrt(n + 1) + 1), 2):
        if n % _ == 0:
            
            r.append(_)

            n /= _
            while n % _ == 0:
                n /= _
                r.append(_)

            return prime(n, r, _ + 2)
    return r + [n]
        
#for _ in range(10**4, 10**5):
#    print _, prime(_,  [], 3)


