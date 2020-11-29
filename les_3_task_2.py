"""
2. Во втором массиве сохранить индексы четных элементов
первого массива. Например, если дан массив со значениями 8, 3,
15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
(помните, что индексация начинается с нуля), т. к. именно в этих
позициях первого массива стоят четные числа.
"""
import random

def ch_index(array):
    ch = 0
    nch = 0
    mas2=[]
    num=0
    ln = len(a)-1
    # print(array)
    # print(ln)
    for x in array:
        if x%2==0:
            # mas2[num]=ch
            mas2.append(ch)
            num += 1
        ch+=1
    return mas2
    # print(mas2)


a=[8,3,15,6,4,2]
print(a)
mas2=ch_index(a)
print(mas2)