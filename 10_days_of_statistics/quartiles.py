def quartiles(arr):
    n = len(arr)    
    arr.sort()
    print arr
    if n % 2:
        return (arr[n / 4 - 1] + arr[n / 4]) / 2, arr[n / 2], (arr[3 * n / 4] + arr[3 * n / 4 + 1]) / 2

    elif (n / 2) % 2:
        return arr[n / 4], (arr[n / 2 - 1] + arr[n / 2]) / 2, arr[3 * n / 4]

    else:
        return (arr[n / 4 - 1] + arr[n / 4]) / 2, (arr[n / 2 - 1] + arr[n / 2]) / 2, (arr[3 * n / 4 - 1] + arr[3 * n / 4]) / 2

print quartiles([4, 17, 7, 14, 18, 12, 3, 16, 10, 4, 4, 12])
