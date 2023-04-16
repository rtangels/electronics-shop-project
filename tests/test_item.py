import pytest

from src.item import Item


def test_calculate_total_price():
    product = Item('Брюква', 2.5, 6)
    assert product.calculate_total_price() == 15.0

def test_apply_discount():
    product = Item('Брюква', 2.5, 6)
    product.pay_rate = 0.8
    product.apply_discount()
    assert product.price == 2