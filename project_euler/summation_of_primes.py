def s(n):
    r = int(n**0.5)
    assert r*r <= n and (r+1)**2 > n
    V = [n//i for i in range(1,r+1)]
    V += list(range(V[-1]-1,0,-1))
    S = {i:i*(i+1)//2-1 for i in V}
    print S
    print
    print
    for p in range(2,r+1):
        print "p is:                 ", p
        print "S[p], S[p-1] is:     ", S[p], S[p-1]
        if S[p] > S[p-1]:  # p is prime
            print "S[p], S[p-1] is:     ", S[p], S[p-1]
            sp = S[p-1]  # sum of primes smaller than p
            p2 = p*p
            print "p2 is:                 ", p2
            for v in V:
                print "v is:                 ", v
                print "v/p is:               ", v/p
                if v < p2: break
                S[v] -= v/p*p*(S[v//p] - sp)
            print S
        print
        print
        print
    return S[n]

print s(10**2)
