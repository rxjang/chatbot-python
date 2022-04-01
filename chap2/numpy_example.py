from re import X
import numpy as np

arr = np.array([1, 2, 3])
print(arr)
print(type(arr))

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)

A = np.array([[1, 2], [3, 4]])
B = np.array([[1, 1], [1, 1]])
C = A + B
print(C)

D = np.array([[1, 2], [3, 4], [5, 6]])
E = np.array([[2, 3], [2, 3]])
F = np.matmul(D, E)
print(F)

d = np.array([[1, 2], [3, 4]])
e = np.array([[1, 1], [1, 1]])
f = d * E
print(f)

A = np.array([[1, 2], [3, 4]])
k = 10
C = k * A
print(C)