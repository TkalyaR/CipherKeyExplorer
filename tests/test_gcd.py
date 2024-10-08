import unittest
from cipherkeyexplorer.main import ex_gcd, mod_inverse


class TestAffineCipher(unittest.TestCase):

    def test_ex_gcd(self):
        # Базовые тесты
        self.assertEqual(ex_gcd(48, 18), (6, -1, 3))
        self.assertEqual(ex_gcd(245, 1584), (1, 653, -101))
        # Тесты с одним нулевым аргументом
        self.assertEqual(ex_gcd(0, 5), (5, 0, 1))
        self.assertEqual(ex_gcd(5, 0), (5, 1, 0))
        # Тесты с отрицательными числами
        # self.assertEqual(ex_gcd(-54, 24), (6, -1, -2))
        # self.assertEqual(ex_gcd(24, -54), (6, 1, -2))
        # self.assertEqual(ex_gcd(-24, -54), (6, -1, -2))
        # Тесты на взаимно простые числа
        self.assertEqual(ex_gcd(35, 64), (1, 11, -6))
        # Тесты на большие числа
        self.assertEqual(ex_gcd(123456, 654321), (3, -46741, 8819))


    
    def test_mod_inverse(self):
        # Тест с большим модулем:
        self.assertEqual(mod_inverse(7, 50), 43)
        # Тест с отрицательным элементом:
        self.assertEqual(mod_inverse(-1, 7) , 6)
        # Тест с взаимно простыми числами:
        self.assertEqual(mod_inverse(10, 21), 19)
        # Тест с одинаковыми a, m
        self.assertEqual(mod_inverse(1, 1), 0)
        self.assertIsNone(mod_inverse(7, 7))
        # Обратного элемента не существует
        self.assertIsNone(mod_inverse(2, 6))
        self.assertIsNone(mod_inverse(0, 6))

if __name__ == '__main__':
    unittest.main()