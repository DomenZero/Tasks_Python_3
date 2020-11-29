"""
4. Определить, какое число в массиве встречается чаще всего
"""

import random


def detect(num):
    ln = len(num) - 1
    rate=[]
    ch=0
    first=num[0]
    k=0
    max_am=0
    max_ch=0
    for i in range(ln):
        # print(first)
        first = num[i]
        if num[i]==first and first!='n':
            for i, item in enumerate(num[:]):
                if num[i] == first and num[i]!='n':
                    ch+=1
                    num[i]='n'
            # print(f'{first},{ch}')
            if max_am<ch:
                max_am=ch
                max_ch=first
            rate.append([k,first,ch])
            k+=1
            ch=0
            # print(num)
    # print(rate)
    return max_ch,max_am


array=[random.randint(2,5) for _ in range(10)]
print(array)
a,b=detect(array)
# print (f'{a,b}')
print(f'Число {a} встречается максимально и = {b}')


