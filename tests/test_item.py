import pytest

from src.item import Item


def test_calculate_total_price():
    product = Item('Телефон', 2.5, 6)
    assert product.calculate_total_price() == 15.0

def test_apply_discount():
    product = Item('Планшет', 2.5, 6)
    product.pay_rate = 0.8
    product.apply_discount()
    assert product.price == 2

def test_instantiate_from_csv():
    """Тестирование метода instantiate_from_csv
                 класса Item"""
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

def test_string_to_number():
    """Тестирование метода string_to_number
                     класса Item"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5.0
    assert Item.string_to_number('5.5') == 5.5
    assert Item.string_to_number('5,5') == 5.5

def test_name():
    """Тестирование метода name
         класса Item"""
    product = Item('Планшет', 2.5, 6)
    assert product.name == 'Планшет'
    product.name = 'Ipad'
    assert product.name == 'Ipad'

def test_str():
    """Тестирование метода __str__"""
    product = Item('Планшет', 10000, 20)
    assert str(product) == 'Планшет'

def test_repr():
    """Тестирование метода __repr__"""
    product = Item('Планшет', 10000, 20)
    assert repr(product) == "Item('Планшет', 10000, 20)"

def test_add():
    """Тестирование метода сложения add"""
    product = Item('Планшет', 10000, 20)
    assert product+product == 40