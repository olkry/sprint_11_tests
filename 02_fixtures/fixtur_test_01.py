import unittest


class Calculator:
    """Производит арифметические действия."""

    def divider(self, num1, num2):
        """Возвращает результат деления num1 / num2."""
        if num2 == 0:
            raise ZeroDivisionError('Не могу делить на ноль')
        return num1 / num2


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""

    # Подготовьте данные для теста при помощи фикстур.
    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator()

    def test_divider(self):
        # вызовите метод divider с валидными аргументами.
        act = self.calc.divider(15, 5)
        self.assertEqual(act, 3, 'текст, если проверка провалена')

    def test_divider_zero_division(self):
        # Проверьте, что деление на 0 выбрасывает исключение
        with self.assertRaises(ZeroDivisionError):
            self.calc.divider(3, 0)
