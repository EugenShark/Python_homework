a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))


def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min([a, b, c]))
    return sum(my_list)


print(my_func(a, b, c))