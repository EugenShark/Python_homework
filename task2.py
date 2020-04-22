def my_func(name, surname, date, city, email, phone):
    print(f"{name} {surname} {date} {city} {email} {phone}")


my_func(input('Введите ваше имя: '), input('Введите вашу фамилию: '), input('Введите год рождения: '), input('Введите город: '), input('Введите алрес эл.почты: '), input('Введите номер телефона: '))


#Вариант 2

#def my_func(name, surname, date, city, email, phone):
#    return f"{name} {surname} {date} {city} {email} {phone}"
#
#
#print(my_func(input('Введите ваше имя: '), input('Введите вашу фамилию: '), input('Введите год рождения: '), input('Введите город: '), input('Введите алрес эл.почты: '), input('Введите номер телефона: ')))