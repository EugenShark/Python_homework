def my_func(x, y):
    exp = 1
    for i in range(abs(y)):
        exp = exp * x
    print(round(1 / exp), 3)


my_func(int(input('Введите целое положительное число: ')), int(input('Введите целое отрицательное число: ')))
