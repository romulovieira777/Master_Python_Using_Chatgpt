import numpy as np


arr_01 = np.array([1, 2, 3, 4])
print(arr_01[0])


arr_02 = np.array([1, 2, 3, 4])
print(arr_02[2] + arr_02[3])


arr_03 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr_03)
print("2nd element on 1st row:", arr_03[0, 1])
print(arr_03[1, 4])
print(arr_03[0, 2])


array_04 = np.array([3, 4, 5, 6])
print(array_04)
print(array_04.ndim)
print(array_04[0])
print(array_04[2])
print(array_04[2] + array_04[0])
