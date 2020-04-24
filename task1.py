from sys import argv

script_name, time, salary, prem = argv

print(f"Ставка: {salary}тг/ч")
print(f"Выработка: {time}ч")
print(f"Премия: {prem}тг")
print(f"Заработная плата сотрудника: {int(salary) * int(time) + int(prem)}тг")
