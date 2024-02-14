import numpy as np


arr_01 = np.array([1, 2, 3, 3, 4, 5, 8, 5, 10, 20, 1])
x = np.where(arr_01 == 1)
print(x)

y = np.where(arr_01 == 4)
print(y)

ans = np.where(arr_01 % 2 == 0)
print(ans)

print(np.sort(arr_01))


arr_02 = np.array([44, 12, 90, 76, 55])
x = np.where(arr_02 == 0)
print(x)

print(np.sort(arr_02))


arr_03 = np.array([3, 2, 0, 1])
print(np.sort(arr_03))


arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))


arr_04 = np.array(['mango', 'papaya', 'apple', 'orange'])
print(np.sort(arr_04))
