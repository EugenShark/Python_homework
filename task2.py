my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(my_list)

new_list = [i for i in my_list[1:] if i > my_list[my_list.index(i) - 1]]
print(new_list)
