month = int(input('Введите номер месяца: '))
year = {'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11), 'Зима': (12, 1, 2)}
for i in year.keys():
    if month in year[i]:
        print(i)