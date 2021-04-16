import numpy as np

matrix: np.ndarray = np.arange(15).reshape(3, 5)
print(matrix)

print(matrix.shape)
print(matrix.ndim)
print(matrix.size)
print(matrix.dtype)
print(matrix.itemsize)
print(matrix.data)
print("=============")

anotherMatrix: np.ndarray = np.array([[1, 2], [1, 2], [3, 4]])
print(anotherMatrix)
print("================")

matrix3: np.ndarray = np.array([[1, 2], [1, 2], [3, 4]],dtype=complex)
print(matrix3)
