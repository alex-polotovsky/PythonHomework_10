"""Создать не менее двух дескрипторов для атрибутов классов,
которые вы создали ранее в ДЗ
"""
class ThisString:
    def __set_name__(self, owner, name):
        self.name = name
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError ('Параметр должен быть строкой.')
        if value == '':
            raise ValueError('Параметр не может быть пустым.')
        instance.__dict__[self.name] = value

class Worker:
    """
    Класс представляет базу данных сотрудников.
    """
    name = ThisString()
    surname = ThisString()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    """
    Класс позволяет получить ФИО сотрудника, его должность и доход.
    """
    def get_full_name(self):
        """
        Функция возвращает полное имя человека.
        :param self: Access the attributes and methods of the class
        :return: The concatenation of the name and surname attributes
        """
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        """
         Функция возвращает общий доход сотрудника компании.
        :param self: Access the instance attributes and methods of the class
        :return: The sum of the incomes in the dictionary
        """
        return sum(self._income.values())

    def __str__(self):
        return f'{self.name} {self.surname}, {self.position}, ' \
               f'доход: {sum(self._income.values())}'


employee_1 = Position('Иван', 'Петров', 'инженер', 70, 30)
employee_2 = Position('Пётр', 'Васильев', 'рабочий', 100, 50)

print(employee_1.get_full_name())
print(f'Полный доход: {employee_1.get_total_income()}')
print()
print(employee_1)
print(employee_2)
