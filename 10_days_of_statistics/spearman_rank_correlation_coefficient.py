def spearman_rank_correlation_coefficient(a, b):
    d_a, d_b = {}, {}
    for i, j in enumerate(sorted(a)): d_a[j] = i
    for i, j in enumerate(sorted(b)): d_b[j] = i
    sum_ranks_squared = 0
    for _ in range(len(a)):
        sum_ranks_squared += (d_a[a[_]] - d_b[b[_]])**2
    print sum_ranks_squared
    return round(1 - (6.0 * sum_ranks_squared) / (len(a) * ((len(a))**2 - 1)), 3)

a= [10.0, 9.8, 8.0, 7.8, 7.7, 1.7, 6.0, 5.0, 1.4, 2.0]

b = [200.0, 44.0, 32.0, 24.0, 22.0, 17.0, 15.0, 12.0, 8.0, 4.0]

print spearman_rank_correlation_coefficient(a, b)
