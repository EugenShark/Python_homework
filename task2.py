name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
date = input('Введите год рождения: ')
city = input('Введите город: ')
email = input('Введите алрес эл.почты: ')
phone = input('Введите номер телефона: ')


def my_func(name, surname, date, city, email, phone):
    return f"{name} {surname} {date} {city} {email} {phone}"


print(my_func(name, surname, date, city, email, phone))
