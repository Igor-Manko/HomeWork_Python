import time


class TrafficLight():

    def __init__(self):
        # приватный атрибут __
        self.__color = ['red', 'yelow', 'green']

    def running(self):

        for color in self.__color:
            if color == self.__color[0]:
                print(color)
                time.sleep(7)
            elif color == self.__color[1]:
                print(color)
                time.sleep(2)
            elif color == self.__color[2]:
                print(color)
                time.sleep(0.5)


traffic_light = TrafficLight()
traffic_light.running()
