from src.item import Item

class Phone(Item):
    """Класс для телефонов"""

    def __init__(self, name, price, quantity, number_of_sim):
        """Инициализирует класс Phone"""
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """Вывод для отладки"""
        return f"Phone('{self.name}', {self.price}, " \
               f"{self.quantity}, {self.number_of_sim})"

    def __str__(self):
        """ Вывод для пользователя"""
        return self.name

    @property
    def number_of_sim(self):
        """Возвращает количество сим карт"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim (self, number):
        """Изменяет количество сим"""
        if number <= 0 or not isinstance(number, int):
             raise ValueError('Количество физических SIM-карт должно'
                             ' быть целым числом больше нуля')
        else:
            self.__number_of_sim = number


