new_list = list(input('Введите произвольный набор букв и цифр: '))
for i in range(1, len(new_list), 2):
    new_list.insert(i - 1, new_list[i])
    new_list.pop(i + 1)
print(new_list)

# new_list = list(input('Введите произвольный набор букв и цифр: '))
# for i in range(1, len(new_list), 2):
# new_list[i - 1], new_list[i] = new_list[i], new_list[i - 1]
# print(''.join([str(i) for i in new_list]))
