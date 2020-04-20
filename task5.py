my_list = [8, 7, 4, 4, 3, 2]
new_rate = int(input('Введите новый рейтинг: '))
for i in my_list:
    if new_rate > i:
        my_list.insert(my_list.index(i), new_rate)
        break
    elif new_rate in my_list:
        my_list.insert(my_list.index(new_rate) + 1, new_rate)
        break
else:
    my_list.append(new_rate)
print(my_list)