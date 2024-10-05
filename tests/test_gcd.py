import pytest
from main import ex_gcd, mod_inverse

def test_ex_gcd():
    # Тестируем различные случаи
    assert ex_gcd(48, 18) == (6, -1, 3)
    assert ex_gcd(18, 18) == (18, 1, 0)
    assert ex_gcd(245, 1584) == (1, 653, -101)
    assert ex_gcd(245, 15) == (5, 1, -16)

def test_mod_inverse():
    # Базовый тест:
    assert mod_inverse(3, 7) == 5
    assert mod_inverse(3, 11) == 4
    # Тест с большим модулем:
    assert mod_inverse(7, 50) == 43
    # Тест с отрицательным элементом:
    assert mod_inverse(-1, 7) == 6
    # Тест с взаимно простыми числами:
    assert mod_inverse(10, 21) == 19

    assert mod_inverse(1, 1) == 0
    assert mod_inverse(2, 6) is None
    assert mod_inverse(2, 2) is None
    assert mod_inverse(0, 6) is None