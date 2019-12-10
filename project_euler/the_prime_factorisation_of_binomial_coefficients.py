#import gmpy2
from math import sqrt, log, floor
from itertools import combinations
from collections import defaultdict

""" Hey Hejo,
You can start with k=1.
You need to seperate two cases:
1- p is a prime that divides binomial(n, m) such that p^2 <= n. In this case use Legendre's formula and just add p to the sum. Those primes with take O(sqrt(n)*log(n)).
2- for primes p such that p^2 > n, v(p)=n/p - m/p - (n-m)/p. v(p) is 0 or 1, and v(p)=1 if and only if p divides binomial(n, m) (this is just Legendre's formula). Now you need to compute sum(on primes sqrt(n)<p<=n)v(p)*p, play with this sum and use what I wrote on the forum. Once you do this, you can extend it to k >= 2. """

def product(iterable):
    p = 1
    for _ in iterable:
        p *= _
    return p

def prime(n, r, start = 3):
    if n == 1: return r
#    if n == 1: return max(r)
    if n % 2 == 0:
        count = 1
        n /= 2
        while n % 2 == 0:
            n /= 2
            count += 1
        return prime(n, [2] * count, 3)
        return prime(n, [2], 3)
    for _ in xrange(start, int(sqrt(n + 1) + 1), 2):
        if n % _ == 0:
            
            r.append(_)

            n /= _
            while n % _ == 0:
                n /= _
                r.append(_)

            return prime(n, r, _ + 2)

#    return r + [n]
    r += [n]
    if len(r) == 1: return True
        
#for _ in range(10**4, 10**5):
#    print _, prime(_,  [], 3)

def binomial_coeffficient(n, k):
    nominator = 1
    denominator = 1
    count = 0
    while count < k:
        nominator *= n
        n -= 1
        count += 1
        denominator *= count
    return nominator / denominator




#print foo(22, 6, 1)

#print binomial_coeffficient(22, 6)
#print prime(binomial_coeffficient(22, 6), [])

# 
def SieveOfEratosthenes(n, m): 
    s = 0
    test = []
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in xrange(n+1)] 
    p = 2
    while (p <= m):

          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in xrange(p * 2, n+1, p): 
                prime[i] = False
        p += 1

    # Print all prime numbers 
    for p in xrange(2, n + 1):
        
        if prime[p]:
            s += p
#            print p, "  ", p
            test.append(p)
#        else: print p
#    return test
    return test, s

#print SieveOfEratosthenes(100, 4)
#print SieveOfEratosthenes(4, 4)
#print [5 * k for k in SieveOfEratosthenes(100/5, 4)]
#print
#print sum(SieveOfEratosthenes(22, 6))
#print sum(SieveOfEratosthenes(100, 4)) - sum([5 * k for k in SieveOfEratosthenes(100/5, 4)]) + 5*sum(SieveOfEratosthenes(4, 4))





def P10(n):
    r = int(n**0.5)
    assert r*r <= n and (r+1)**2 > n
    V = [n//i for i in range(1,r+1)]
    V += list(range(V[-1]-1,0,-1))
    S = {i:i*(i+1)//2-1 for i in V}
    for p in range(2,r+1):
        if S[p] > S[p-1]:  # p is prime
            sp = S[p-1]  # sum of primes smaller than p
            p2 = p*p
            for v in V:
                if v < p2: break
                S[v] -= p*(S[v//p] - sp)
    return S[n]



def prime_of_binomial_coefficient(n, k):
    n_original = n
#    n = int(sqrt(n))
    r = []
    d = defaultdict(int)
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in xrange(n+1)] 
    p = 2
    while (p <= n):

          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in xrange(p * 2, n+1, p): 
                prime[i] = False
        p += 1

    # Print all prime numbers 
    for p in xrange(2, n):

        if prime[p]:


            tmp_n = n_original
            tmp_k = k
            tmp_n_k = n_original - k

            while tmp_n / p > 0:
                d[p] += tmp_n / p
                tmp_n /= p

            while p <= k and tmp_k / p > 0:
                d[p] -= tmp_k / p
                tmp_k /= p

            while p <= n - k and tmp_n_k / p > 0:
                d[p] -= tmp_n_k / p
                tmp_n_k /= p

#            if p < n:
#                while tmp_n / p > 0:
#                    d[p] += tmp_n / p
#                    tmp_n /= p

#                while p <= k and tmp_k / p > 0:
#                    d[p] -= tmp_k / p
#                    tmp_k /= p

#                while p <= n_original - k and tmp_n_k / p > 0:
#                    d[p] -= tmp_n_k / p
#                    tmp_n_k /= p
#                for _ in d:
#                    if d[_] > 0: r.append(_)

            if tmp_n / p - tmp_k / p - tmp_n_k / p == 1: r.append(p)
#    return r
#    return d
    return [k for k in d if d[k] != 0], product([k for k in d if d[k] != 0])
#    return len([k for k in d if d[k] != 0])
##    return sum([k for k in d if d[k] != 0])
#    p = 1
#    s = 0
#    for _ in d:
#        if d[_] > 0:
#            p *= _**d[_]
##            s += _*d[_]
#    print p, int(log(p, 10)) + 1
##    return s


##    return p, int(log(p, 10)) + 1



print prime_of_binomial_coefficient(22, 6)




#def prime_of_binomial_coefficient2(n, k):
#    r = []
#    d = defaultdict(int)

#    p = 2

#    while p < sqrt(n) + 1:

#        tmp_n = n
#        tmp_k = k
#        tmp_n_k = n - k


#        if p < sqrt(n):
#            while tmp_n / p > 0:
#                d[p] += tmp_n / p
#                tmp_n /= p

#            while p <= k and tmp_k / p > 0:
#                d[p] -= tmp_k / p
#                tmp_k /= p

#            while p <= n - k and tmp_n_k / p > 0:
#                d[p] -= tmp_n_k / p
#                tmp_n_k /= p


##        elif tmp_n / p - tmp_k / p - tmp_n_k / p == 1:
##            r.append(p)

#        p = int(gmpy2.next_prime(p))
#    for _ in d:
#        if d[_] > 0: r.append(_)

#    return r




def foo(N, M, k):
    return sum(map(product, (combinations(prime_of_binomial_coefficient(N, M), k)))) % 1004535809

#print prime_of_binomial_coefficient(10, 6) 
##print list(combinations([3,7,11,17,19], 4))
#print P10(15)

def prime_number_generator(n):
    r = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    for p in xrange(32, n + 1):
        for d in r:
            critical = int(sqrt(p)) + 1
            if d < critical and p % d == 0: break
            if d >= critical: r.append(p); break 
    return r

#print prime_number_generator(10**6)

#print [0] * 10**8


#n = 1004535805499481

        
#print  prime(n, [])

#print product(prime(n, [])) == n

#print sqrt(n)




def digits_of_a_number(n):
    return 1 + int(log(n, 10))

#print digits_of_a_number(10000)



def all_divisors(n):
    r = []
    for _ in range(2, int(sqrt(n)) + 1):
        if not n % _: r.append(_); r.append(n / _)
    return r



#print SieveOfEratosthenes(22 / 3, 2)


























