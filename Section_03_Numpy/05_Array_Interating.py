import numpy as np


arr_01 = np.array([1, 2, 3, 4, 5])

for x in arr_01:
    print(x)


arr_02 = np.array([[1, 2, 3], [4, 5, 6]])

for i in arr_02:
    print(i)

for x in arr_02:
    for y in x:
        print(y)
