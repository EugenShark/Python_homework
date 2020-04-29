with open("text_3.txt", encoding="utf-8") as read:
    a = read.read()
    my_list = a.split('\n')
    salary = []
    less = []
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            less.append(i[0])
        salary.append(i[1])
average = sum(map(float, salary)) / len(salary)
names = ', '.join(less)
print(f'У сотрудников {names} оклад ниже 20000. Средний доход по штату: {average}')
