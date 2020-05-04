class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f"Полное имя сотрудника: {self.position} {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Поная зарплата сотрдника: {self._income.get('wage') + self._income.get('bonus')}тг")


a = Position('Ivan', 'Petrov', 'Engineer', 25000, 5000)
a.get_full_name()
a.get_total_income()
b = Position('Petr', 'Ivanov', 'Courier', 13000, 3000)
b.get_full_name()
b.get_total_income()
