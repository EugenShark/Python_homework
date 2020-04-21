def div_func(a, b):
    try:
        return round(a / b, 3)
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'

print(div_func(int(input('Введите первое число')), int(input('Введите второе число'))))