"""Создать не менее двух дескрипторов для атрибутов классов,
которые вы создали ранее в ДЗ
"""
class ThisDigit:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError('Параметр должен быть числом')
        if value < 0:
            raise ValueError('Параметр не может быть отрицательным.')
        instance.__dict__[self.name] = value

class Road:
    """
    Класс определяет параметры асвальтового покрытия дороги.
    """
    length = ThisDigit()
    width = ThisDigit()

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def mass_of_asphalt(self, udmass, thikness):
        """
        Функция вычисляет массу асфальта, необходимого для покрытия им дороги.
        Она принимает два аргумента: udmass и thikness.
        Функция возвращает общую массу требуемого асфальта.

        :param self: Represent the instance of the class
        :param udmass: Удельная масса асфальта (1м^2 дороги толщиной 1см
        :param thikness: Необходимая толщина покрытия
        :return: The mass of asphalt required to cover the road
        """
        self.udmass = udmass
        self.thikness = thikness
        return self._length * self._width * self.udmass * self.thikness


my_road = Road(500, 20)

print('Масса асфальта: ', my_road.mass_of_asphalt(25, 0.05))
print(my_road.udmass, my_road.thikness)
