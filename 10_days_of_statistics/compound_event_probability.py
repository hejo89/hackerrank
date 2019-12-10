from fractions import *

X = [4, 3]

Y = [5, 4]

Z = [4, 4]

c = 0
for i in range(2):
    for j in range(2):
        for k in range(2):
            if sorted([i, j, k]) == [0, 0, 1]:
                c += Fraction(X[i] , sum(X)) * Fraction(Y[j] , sum(Y)) * Fraction(Z[k] , sum(Z))

print c
