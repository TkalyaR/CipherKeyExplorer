import unittest
from cipherkeyexplorer import mod_inverse, ex_gcd

class TestAffineCipher(unittest.TestCase):

    def test_ex_gcd(self):
        # Тестируем различные случаи
        self.assertEqual(ex_gcd(48, 18), (6, -1, 3))
        self.assertEqual(ex_gcd(18, 18), (18, 1, 0))
        self.assertEqual(ex_gcd(245, 1584), (1, 653, -101))
        self.assertEqual(ex_gcd(245, 15), (5, 1, -16))
    
    def test_mod_inverse(self):
        # Базовый тест:
        self.assertEqual(mod_inverse(3, 7), 5)
        self.assertEqual(mod_inverse(3, 11) , 4)
         # Тест с большим модулем:
        self.assertEqual(mod_inverse(7, 50), 43)
         # Тест с отрицательным элементом:
        self.assertEqual(mod_inverse(-1, 7) , 6)
        # Тест с взаимно простыми числами:
        self.assertEqual(mod_inverse(10, 21), 19)

        self.assertEqual(mod_inverse(1, 1), 0)
        self.assertIs(mod_inverse(2, 6), None)
        self.assertIs(mod_inverse(2, 2), None)
        self.assertIs(mod_inverse(0, 6), None)

if __name__ == '__main__':
    unittest.main()