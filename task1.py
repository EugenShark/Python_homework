new_list = []
while 1:
    new_data = input("Введите данные: ")
    if new_data == '':
        print(new_list)
        exit()
    else:
        new_list.append(new_data + "\n")
        print(new_list)
    new_file = open("my_file.txt", "w")
    new_file.writelines(new_list)
    new_file.close()
