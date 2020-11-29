"""
3. В массиве случайных целых чисел поменять местами
минимальный и максимальный элементы.
"""

import random

def min_max(array):
    max=array[0]
    min=array[0]
    i=0
    k=0
    n=0
    ln = len(array) - 1
    for i in range(ln):
        if max<array[i]:
            max=array[i]
            k=i
        if min>array[i]:
            min=array[i]
            n=i

    array[k], array[n] = array[n], array[k]
    print(f'{min}-{n},{max}-{k}')
    # print(array)
    return array


array=[random.randint(-100,100) for _ in range(10)]

print(array)
print(min_max(array))

