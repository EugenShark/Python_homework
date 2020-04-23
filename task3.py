def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min([a, b, c]))
    return sum(my_list)


print(my_func(int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье число: '))))