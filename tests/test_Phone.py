from src.Phone import Phone


def test_init():
    product = Phone('yota 7', 10000, 20, 1)
    assert product.quantity == 20

def test_repr():
    """Тестирование метода __repr__"""
    product = Phone('yota 7', 10000, 20,1)
    assert repr(product) == "Phone('yota 7', 10000, 20, 1)"
def test_str():
    """Тестирование метода __str__"""
    product = Phone('yota 7', 10000, 20,1)
    assert str(product) == 'yota 7'

def test_name():
    """Тестирование метода name"""
    product = Phone('yota 7', 10000, 20, 1)
    assert product.name == 'yota 7'

def test_number_of_sim ():
    """Тестирование функции изменения кол-ва sim"""
    product = Phone('yota 7', 10000, 20, 1)
    assert product.number_of_sim == 1

    product.number_of_sim = 2
    assert product.number_of_sim == 2







