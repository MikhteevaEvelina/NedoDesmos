import unittest
# запустить тесты  python.exe -m unittest tests.py 

from funk import solving_eq

class Test_solvingeq(unittest.TestCase):
    def test_all(self):
        self.assertEqual(solving_eq(0, 0, 0), ["Решением данного уравнения является вся числовая прямая"])

    def test_no1(self):
        self.assertEqual(solving_eq(0, 0, 1), ["Уравнение не имеет решений"])

    def test_no2(self):
        self.assertEqual(solving_eq(1, 1, 1), ["Уравнение не имеет решений в действительных числах"])

    def test_line(self):
        self.assertEqual(solving_eq(0, 5, 1), ["Уравнение имеет единственное решение", "x = -0.2"])

    def test_oneres(self):
        self.assertEqual(solving_eq(1, 2, 1), ["Уравнение имеет единственное решение", "x = -1.0"])

    def test_twores(self):
        self.assertEqual(solving_eq(1, 0, -4), ["Уравнение имеет два решения", "x1 = 2.0", "x2 = -2.0"])
    