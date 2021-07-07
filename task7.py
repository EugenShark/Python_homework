from itertools import count
from math import factorial


def generator():
    for el in count(1):
        yield factorial(el)


g = generator()
x = int(input('Введите факториал какого числа вы хотите получить: '))
y = 0
for i in g:
    if y < x:
        print(i)
        y += 1
    else:
        break
