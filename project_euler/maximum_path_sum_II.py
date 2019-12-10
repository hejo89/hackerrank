#T = int(raw_input())
#for _ in range(T):
#    n = int(raw_input())
#    N = []
#    for j in range(n):
#        N.append(map(int, raw_input().split(" ")))
#    print N


arr = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]

def maximum_path_sum(arr):
    for k, _ in enumerate(arr[1:]):
        for i, j in enumerate(_):
            if i == 0:
                _[0] += arr[k][0]
            elif i == len(_) - 1:
                _[i] += arr[k][-1]
            elif i < len(_) - 1 or i > 0:
                _[i] += max(arr[k][i - 1], arr[k][i])
    return max(arr[-1])
print maximum_path_sum(arr)
        
