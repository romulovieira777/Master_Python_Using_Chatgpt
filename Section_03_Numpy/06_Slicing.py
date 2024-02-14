import numpy as np

arr_01 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr_01)
print(arr_01[1:5])
print(arr_01[2:7])
print(arr_01[4:])
print(arr_01[:5])
print(arr_01[1:6:2])

arr_02 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr_02[1, 1:4])
print(arr_02[0, 0, 2])
