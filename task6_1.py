from itertools import count

i_start = int(input('Введите сартовое число: '))
i_end = int(input('Введите финишное число: '))
for i in count(i_start):
    if i > i_end:
        break
    else:
        print(i)
