import unittest


class Calculator:
    """Производит арифметические действия."""

    def summ(self, *args):
        """
        Возвращает сумму принятых аргументов,
        если аргументов нет, возвращает None.
        """
        if len(args) == 0:
            return None
        return sum(args)


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""

    @classmethod
    def setUpClass(cls):
        """Вызывается один раз перед запуском всех тестов класса."""
        cls.calc = Calculator()

    def test_summ(self):
        act = self.calc.summ(3, 5, 2, 3, 7)
        self.assertEqual(act, 20, 'test_summ fall')

    def test_summ_no_argument(self):
        act = self.calc.summ()
        self.assertIsNone(act, 'test_summ_no_argument fall')

    def test_summ_one_argument(self):
        act = self.calc.summ(12)
        self.assertEqual(act, 12, 'test_summ_one_argument fall')