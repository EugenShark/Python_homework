month = int(input('Введите номер месяца: '))
year = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2]
if month in year[0:3]:
    print('Весна')
elif month in year[3:6]:
    print('Лето')
elif month in year[6:9]:
    print('Осень')
elif month in year[9:]:
    print('Зима')
else:
    print('Такого месяца не существует')
