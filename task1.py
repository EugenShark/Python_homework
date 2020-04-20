print('Типы данных из списка')
my_list = [3, 5.8, 'важная строка', [13, 21, 34], ('к', 'о', 'р', 'т'), {55, 89, 144}, {'key_1': 'value_1', 'key_2': 'value_2'}, False]
print(f"Исходные данные: {my_list}")
print(f"Тип исходных данных: {type(my_list)}")
for i in range(len(my_list)):
    print(f"Тип элемента *{my_list[i]}*: {type(my_list[i])}")