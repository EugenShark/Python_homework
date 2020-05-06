class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        t = float(input("Введите толщину покрытия в см: "))
        m = self._length * self._width * 0.025 * t
        print(f"Масса асфальта: {m}т")


my_road = Road(20, 5000)
my_road.calc()
