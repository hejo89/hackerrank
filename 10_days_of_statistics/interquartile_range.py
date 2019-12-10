#n = int(raw_input())
#arr = map(int, raw_input().split())
#frequencies = map(int, raw_input().split())
frequencies = range(1, 11)
arr = [10, 40, 30, 50, 20, 10, 40, 30, 50, 20]
array = [k for i, k in enumerate(arr) for j in range(frequencies[i])]

def interquartile_range(arr):
    n = len(arr)
    arr.sort()
    if n % 2 and not (n - 1 / 2) % 2:
        return -(arr[n / 4 - 1] + arr[n / 4]) / 2.0 + (arr[3 * n / 4] + arr[3 * n / 4 + 1]) / 2.0
    if n % 2 and (n - 1 / 2) % 2:
        return -(float(arr[n / 4])) + float(arr[3 * n / 4])
    if not n % 2 and (n / 2) % 2:
        return -(float(arr[n / 4])) + float(arr[3 * n / 4])

    else:
        return -(arr[n / 4 - 1] + arr[n / 4]) / 2.0 + (arr[3 * n / 4 - 1] + arr[3 * n / 4]) / 2.0

print interquartile_range(array)
