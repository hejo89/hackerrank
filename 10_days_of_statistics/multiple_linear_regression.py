from numpy import *
from numpy.linalg import inv

a = array([[1,2], [3,4]])
#print(a)
#print(inv(a))
#print(transpose(a))

def weights(X, Y):
#    print(X)
#    print(Y)
#    return dot(dot(inv(dot(transpose(X), X)), transpose(X)), Y)
    return matmul(matmul(inv(matmul(X, transpose(X))), X), Y)

with open("multiple_linear_regression_test_case1.txt", "r") as f:
    n, m = map(int, f.readline().strip().split())
    X, Y = [], []

    for _ in range(m):
        tmp = list(map(float, f.readline().strip().split()))
        X.append([1] + tmp[:-1])
        Y.append(tmp[-1])
#    print(X)
    X = array(list(zip(*X)))
    Y = array(Y)
    w = weights(X, Y)
#    print(X)
#    print(Y)
    q = int(f.readline().strip())
    for _ in range(q):
        tmp = array([1] + list(map(float, f.readline().strip().split())))
        print(matmul(tmp, transpose(w)))



#X = array([[1] * 5, [5, 6, 7, 8, 9], [7, 6, 4, 5, 6]])
#Y = array([10, 20, 60, 40, 50])
#X = array([[1, 1, 1, 1, 1, 1, 1], [0.18, 1.0, 0.92, 0.07, 0.85, 0.99, 0.87], [0.89, 0.26, 0.11, 0.37, 0.16, 0.41, 0.47]])
#Y = array([109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77])
#print(X)
#print(transpose(X))
#print(weights(X, Y))
