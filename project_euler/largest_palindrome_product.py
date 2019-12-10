from math import sqrt

def sieve_of_erastothenes(m, n):
    final = [0] * (n + 1)
    p = [True] * (n + 1)

    for _ in xrange(2, int(sqrt(n) + 1)):
        if p[_] == True:
            for __ in xrange(_**2, n + 1, _):
                p[__] = False

    return [k for k in xrange(m, n + 1) if p[k] == True]

#print sieve_of_erastothenes(2, 10**2)



def P10(n):
    r = int(n**0.5)
    assert r*r <= n and (r+1)**2 > n
    V = [n//i for i in range(1,r+1)]

    V += list(range(V[-1]-1,0,-1))
    print V
    print
    S = {i:i*(i+1)//2-1 for i in V}
    print S
    print
    for p in range(2,r+1):
        if S[p] > S[p-1]:  # p is prime
            sp = S[p-1]  # sum of primes smaller than p
            p2 = p*p
            print p, p2, S[p], sp
            for v in V:
                if v < p2: break
                S[v] -= p*(S[v//p] - sp)
                print S
    return S[n]

print P10(100)
