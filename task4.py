new_list = str(input('Введите несколько слов через пробел: ')).split()
for i, num in enumerate(new_list, 1):
    if len(new_list) >= 10:
        print(i, num)
    else:
        print(i, num[0:10])