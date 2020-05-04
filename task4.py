class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} начала движение")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name} повернула на{direction}")

    def show_speed(self, speed):
        print(f"Скорость автомобиля {self.name} {speed}км/ч")


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60 and self.is_police is False:
            print(f"Скорость автомобиля {self.name}: {self.speed}км/ч. Внимание! Скорость превышена!")
        else:
            print(f"Скорость автомобиля {self.name}: {self.speed}км/ч")


b = TownCar(70, "Red", "Nick", False)
b.go()
b.show_speed()
b.turn("право")

d = TownCar(70, "Black", "Willi", True)
d.show_speed()
d.turn("лево")
d.stop()


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


e = SportCar(210, "Blue", "Bob", False)
e.go()
e.turn("право")


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40 and self.is_police is False:
            print(f"Скорость автомобиля {self.name}: {self.speed}км/ч. Внимание! Скорость превышена!")
        else:
            print(f"Скорость автомобиля {self.name}: {self.speed}км/ч")


f = WorkCar(30, "White", "Ed", False)
f.go()
f.show_speed()
f.turn("право")


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
