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
    dis_first=-1
    for i in range(ln):
        if array[i]<dis and array[i]<0:
            dis=i
        elif array[i]<0 and array[i]>array[dis]:
            dis=i
        if dis_first==-1 and array[i]<0:
            dis_first=i
        elif array[i]<0 and array[i]>array[dis_first]:
            dis_first=i



    print(f'На позиции {dis} лежит максимально отрицательный элемент {array[dis]}')
    print(f'На позиции {dis_first} лежит ближайший отрицательный элемент {array[dis_first]}')
array=[random.randint(-100,100) for _ in range(10)]

print(array)
max_dis(array)

