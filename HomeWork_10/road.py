class Road():

    # защищенный атрибут _
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        mass = self._lenght * self._width * self.weight * self.height
        print(f'Масса асфальта: {int(mass / 1000)} т.')


weight = Road(5000, 20)
weight.asphalt_mass()
