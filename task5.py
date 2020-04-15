print('Прибыль и убыток')
rev = float(input('Введите выручку компании: '))
cost = float(input('Введите издержки компании: '))
if rev > cost:
    print('Компания в прибыли!')
    profit = (rev / cost - 1) * 100
    print(f"Рентабельность компании: {profit:.2f}%!")
    empl = int(input('Введите число сотрудников: '))
    fee = (rev - cost) / empl
    print(f"Прибыль на одного сотрудника: {fee:.3f}")
else:
    print('У компании убытки!')