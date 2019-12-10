import time
def matrix_multiplication(A, B, mod_calculation, mod):
    if len(A[0]) != len(B):
        print "Matrices not compatible for multiplication! \n" ,"Matrix A has", len(A[0]), "columns. \n", "Matrix B has", len(B), "rows."
        return

    C = [[0] * len(B[0]) for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            s = 0
            for k in range(len(A[0])):
#                if mod_calculation == "yes":    s += ((A[i][k] % mod) * (B[k][j] % mod)) % mod
#                else:                           s += A[i][k] * B[k][j]
                s += A[i][k] * B[k][j]
            if mod_calculation == "yes":
                C[i][j] = s % mod
            else: C[i][j] = s

    return C


def matrix_exponentiation_loop(M, k, mod_calculation, mod):
    if k < 0 or type(k) != int: print "Please enter 0 or a positive integer for k"; return 
    if k == 0: return [[1 if item_idx == row_idx else 0 for item_idx in range(0, 3)] for row_idx in range(0, 3)]
    tmp = M
    for _ in range(k - 1):
        tmp = matrix_multiplication(M, tmp, mod_calculation, mod)
    return tmp

def matrix_exponentiation(M, k, mod_calculation, mod):
    if k < 0 or type(k) != int: print "Please enter 0 or a positive integer for k"; return 
    if k == 0: return [[1 if item_idx == row_idx else 0 for item_idx in range(0, len(M))] for row_idx in range(0, len(M))]
    power_2_matrices = [M]
    tmp = M
    for _ in range(len(bin(k)[2:]) - 1):
        tmp = matrix_multiplication(tmp, tmp, mod_calculation, mod)
        power_2_matrices.append(tmp)
#    print len(power_2_matrices), len([_ for _ in bin(k)[2:] if _ == "1"])
    power_2_matrices = [j for i, j in enumerate(power_2_matrices) if bin(k)[2:][::-1][i] == "1"]
    result = power_2_matrices[-1]
    for i in range(len(power_2_matrices) - 1):
        result = matrix_multiplication(result, power_2_matrices[i], mod_calculation, mod)
    return result

def fib(n, mod_calculation, mod):
    if n == 0: return 0

    return matrix_multiplication([[1, 1]], matrix_exponentiation([[0, 1], [1, 1]], n - 1, mod_calculation, mod), mod_calculation, mod)[0][0]

#arr = [[0, 1], [1, 1]]
arr = [[2,-1,0,1], [1,0,0,0], [0,1,0,0], [0,0,1,0]]
arr = [[1,1,0,0,0, 0],[0,0,1,0,0,0], [0,0,0,1,0,0], [0,0,0,0,1, 0], [0,0,0,0,0,1], [1,0,0,0,0,1]]

modulo = 10**15 + 7

#time_start = float(time.time())

##print matrix_exponentiation(arr, 0, "n", modulo)
#print fib(10**19, "yes", modulo)

#print float(time.time()) - time_start

#time_start = float(time.time())
#print matrix_exponentiation_loop(arr, 10**9,  "yes", modulo)
#print float(time.time()) - time_start


#print matrix_multiplication([[1,1,1,1, 1, 1]], matrix_exponentiation(arr, 50, "n", modulo), "n", 4)
#print matrix_exponentiation(arr, 50, "n", modulo) 


def matrix(m):
    first = [[1, 1] + (m - 1) * [0]]
    last = [[1] + [0] * (m - 1) + [1]]
    
    for _ in range(m - 1):

        first += [[0] * (_ + 2) + [1] + [0] * (m - 2 - _)]
    return first + last, [[1] * (m + 1)]


def block_combinations(n, m, mod_calculation, mod):
    a, b = matrix(m)
    return matrix_multiplication(b, matrix_exponentiation(a, n, mod_calculation, mod), mod_calculation, mod)

print block_combinations(50, 3, "no", 7)[0][-2]














