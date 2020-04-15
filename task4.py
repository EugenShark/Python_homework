print('Самая большая цифра')
numa = int(input('Введите целое положительное число: '))
maxnum = numa % 10
numb = numa // 10
while numb > 0:
    if numb % 10 > maxnum:
        maxnum = numb % 10
    numb = numb // 10
print(f"Самая большая цифра в числе: {maxnum}")