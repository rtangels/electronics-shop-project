from src.item import Item

if __name__ == '__main__':
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    # Exception: Длина наименования товара превышает 10 символов.

    Item.instantiate_from_csv()  # создание объектов из данных файла

    assert len(Item.all) == 6  # в файле 6 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    # не знаю, можно ли было менять, но так как цена у нас может
    #быть числом с плавающей точкой я решил, что и метод в классе
    #должен возвращать числа с плавающей точкой
    assert Item.string_to_number('5.5') == 5.5
