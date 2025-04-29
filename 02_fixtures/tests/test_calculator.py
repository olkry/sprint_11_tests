import unittest

# Импортируем класс MadCalculator.
from calc_code.calculator import MadCalculator


class TestCalc(unittest.TestCase):
    """Тестируем MadCalculator."""

    '''def setUp(self):
        """Подготовка прогона теста. Вызывается перед каждым тестом."""
        # Arrange - подготавливаем данные для каждого теста.
        self.calc = MadCalculator()
        print(self.calc)'''

    @classmethod  # Декорируем метод класса.
    def setUpClass(cls):
        """Вызывается один раз перед запуском всех тестов класса."""
        # Для создания объекта и обращения к нему вместо self применяем cls.
        cls.calc = MadCalculator()
        print(cls.calc)  # Обращаемся к объекту не self.calc, а cls.calc.

    def test_sum_string(self):
        """Тестирование функции sum_string с конкатенацией строк."""
        act = self.calc.sum_string(1, 100500)
        # Сравниваем фактический результат с ожидаемым.
        self.assertEqual(
            act, 1100500, 'Метод sum_string работает неправильно.')

    def test_sum_string_negative_value(self):
        """Тестирование исключения с отрицательным числом."""
        # Проверяем, что тест выдаст ошибку ValueError.
        with self.assertRaises(ValueError):
            self.calc.sum_string(1, -100500)

    def test_sum_args(self):
        """Тестирование функции суммирования аргументов."""
        act = self.calc.sum_args(3, -3, 5)
        self.assertEqual(act, 5, 'Метод sum_args работает неправильно.')
