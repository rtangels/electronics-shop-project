import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)


    def __repr__(self):
        """Возвращает  вывод для Item"""
        return f"""Item('{self.name}', {self.price}, {self.quantity})"""

    def __str__(self):
        """Возвращает вывод для пользователей"""
        return f"{self.name}"


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price*self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price*self.pay_rate

    @classmethod
    def  instantiate_from_csv(cls):
        """ Инициализирующий экземпляры класса Item данными из файла"""
        #создадим лист, куда поместим экземпляры класса
        list_item = []
        with open("../src/items.csv") as file:
            CsvDictReader = csv.DictReader(file, delimiter=",")
            for line in CsvDictReader:
                name = line['name']
                price = line['price']
                quantity = line['quantity']
                list_item.append(cls(name, price, quantity))
            return list_item


    @staticmethod
    def string_to_number(number_string: str):
        """"Функция переводит из числа строки
                     в число"""
        # Проверка на случай если строка-число может оказаться
        # числом с плавающей точкой
        if '.' in number_string:
            number = float(number_string)
        elif ',' in number_string:
          number_string=number_string.replace(',', '.')
          number = float(number_string)
        else:
            number = int(number_string)
        return number

    def __add__(self, other):
        """Реализует сложение по количеству на складе"""
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise Exception('невозможно складывать с данным классом')

    @property
    def name(self):
        """Возвращает название товара"""
        return self.__name
    @name.setter
    def name (self, name_word):
        """ Изменяет название товара"""
        if len(name_word) <= 10:
            self.__name = name_word
        else:
            Exception('Длина наименования товара превышает 10 cимволов')