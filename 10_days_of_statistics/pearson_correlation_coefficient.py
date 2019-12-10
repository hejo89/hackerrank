def mean(arr):
    return float(sum(arr)) / len(arr)

def sd(arr):
    mu = mean(arr)
    return pow(float(sum([(x - mu)**2 for x in arr])) / len(arr), 0.5)

def pearson_correlation_coefficient(a, b):
    mu_a, mu_b = mean(a), mean(b)
    return round(float(sum([(a[i] - mu_a) * (b[i] - mu_b) for i in range(len(a))])) / (len(a) * sd(a)  *sd(b)), 3)

a = [10.0, 9.8, 8.0, 7.8, 7.7, 7.0, 6.0, 5.0, 4.0, 2.0]

b = [200.0, 44.0, 32.0, 24.0, 22.0, 17.0, 15.0, 12.0, 8.0, 4.0]

print pearson_correlation_coefficient(a, b)
print mean(a), mean(b)
print sd(a), sd(b)
