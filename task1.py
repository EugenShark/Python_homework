from time import sleep


class TrafficLight:

    __color = {'Red': 7, 'Yellow': 2, 'Green': 5}

    def running(self):
        print("Светофор запущен")
        for key in TrafficLight.__color:
            print(key)
            sleep(TrafficLight.__color[key])


my_tl = TrafficLight()
my_tl.running()
