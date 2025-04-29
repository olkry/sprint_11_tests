import unittest


def bartender(order):
    if isinstance(order, int) and order > 0:
        return order
    return 'Извините, я не могу вас обслужить!'


class TestBar(unittest.TestCase):

    def test_bartender(self):
        barmens_ansver = 'Извините, я не могу вас обслужить!'
        values_results = (
            (5, 5),
            (0, barmens_ansver),
            (0.33, barmens_ansver),
            (-1.999999, barmens_ansver),
            ('фываолдж', barmens_ansver)
        )
        for value, expected_result in values_results:
            with self.subTest():
                result = bartender(value)
                self.assertEqual(result, expected_result)
