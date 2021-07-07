my_list = [2, 23, 4, 5, 6, 2, 75, 6, 2, 23, 23, 23, 1]
new_list = [i for i in my_list if my_list.count(i) < 2]

print(new_list)