"""
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный»
и «максимальный отрицательный». Это два абсолютно разных значения.
"""

import random

def max_dis(array):
    i=0
    k=0
    n=0
    ln = len(array) - 1
    dis=-1
    for i in range(ln):
        if array[i]<dis and array[i]<0:
            dis=i
        elif array[i]<0 and array[i]>array[dis]:
            dis=i


    print(f'На позиции {dis} лежит максимально отрицательный элемент {array[dis]}')


array=[random.randint(-100,100) for _ in range(10)]

print(array)
max_dis(array)

