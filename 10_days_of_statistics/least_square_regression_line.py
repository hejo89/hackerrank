import random
import matplotlib.pyplot as plt
def least_sqaure_regression(a, b, regression = None):
    sum_xy = sum([a[i] * b[i] for i in range(len(a))])
    sum_x = sum(a)
    sum_y = sum(b)
    sum_x_squared = sum([x**2 for x in a])
    n = len(a)

    slope = float((n * sum_xy - sum_x*sum_y)) / (n * sum_x_squared - sum_x**2)
    intercept = float(sum_y) / n  - slope * float(sum_x) / n
    if regression or regression == 0: return round(intercept + slope * regression, 5)
    return intercept, slope
a, b = [], []

for _ in range(10**2): a.append(random.choice(range(10**2)))
for _ in range(10**2): b.append(random.choice(range(10**2)))
plt.plot(a, b, "bo")

print(least_sqaure_regression(a, b))
plt.show()
