"""
1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
"""
def count_div(count):
    ch = 0
    i=count
    print(f'Числу: {count}')
    while i<100:
        if (i % count) == 0 and (count)<100:
            ch += 1
            # print(f' UI: {((i))}')
        i+=1

    return ch

array=[2,3,4,5,6,7,8,9]
i=2
ii=0
while i<10:
     print(f' Кратно: {int(count_div(i))}')
     i+=1

