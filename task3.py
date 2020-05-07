class Cell:

    def __init__(self, number):
        self.count = number

    def __str__(self):
        return str(self.count)

    def __add__(self, other):
        return f"Ячеек в новой клетке: {Cell(self.count + other.count)}"

    def __sub__(self, other):
        new_size = self.count - other.count
        if new_size > 0:
            return f"Ячеек в новой клетке: {Cell(new_size)}"
        else:
            return "Количество ячеек новой клетки меньше нуля!"

    def __mul__(self, other):
        return f"Ячеек в новой клетке: {Cell(self.count * other.count)}"

    def __truediv__(self, other):
        return f"Ячеек в новой клетке: {Cell(self.count // other.count)}"

    def make_order(self, numbers_of_row):
        pass


c3 = Cell(3)
c4 = Cell(4)
print(c3 + c4)
print(c3 - c4)
print(c4 - c3)
print(c3 * c4)
print(c4 / c3)
