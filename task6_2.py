from itertools import cycle

my_list = [0, 1, 1, 2, 3, 5, 8, 13, 21]
a = 0
b = int(input('Введите количество значений: '))
for i in cycle(my_list):
    if a > b:
        break
    print(i)
    a += 1
