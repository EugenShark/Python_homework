print('Переводчик времени')
time = int(input('Введите время в секундах: '))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time % 60
print(f"Ваше время: {hours:02d}:{minutes:02d}:{seconds:02d}")