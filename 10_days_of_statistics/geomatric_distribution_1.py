n = 1
d = 3
p = float(n) / d
P = 0
for j in range(1, 5 + 1):
    P += p * (1 - p)**(5  - j)
print round(P, 3)

