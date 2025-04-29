
class Contact:

    def __init__(self, name, year_birth, is_programmer):
        self.name = name
        self.year_birth = year_birth
        self.is_programmer = is_programmer

    def age_define(self):
        if 1946 < self.year_birth < 1980:
            return 'Олдскул'
        if self.year_birth >= 1980:
            return 'Молодой'
        return 'Старейшина'

    def programmer_define(self):
        if self.is_programmer:
            return 'Программист'
        return 'Нормальный'

    def show_contact(self):
        return (
            f'{self.name}, '
            f'возраст: {self.age_define()}, '
            f'статус: {self.programmer_define()}'
        )


# Создайте экземпляр класса Contact с необходимыми параметрами.
# Например, test_old_none_programmer = Contact('Пушкин', 1799, False).
test_old_none_programmer = Contact('Пушкин', 1799, False)


# Напишите assert и в нём проверьте,
# что метод programmer_define() этого экземпляра возвращает строку "Нормальный".
# Во втором assert проверьте, возвращает ли метод age_define() значение "Старейшина".
assert test_old_none_programmer.programmer_define(
) == 'Нормальный', 'Ошибка programmer_define()'
assert test_old_none_programmer.age_define() == 'Старейшина', 'Ошибка age_define()'
# Создайте новый экземпляр с другими параметрами;
# через assert проверьте, вернут ли и его методы ожидаемый результат.
aden = Contact('Олег', 1990, True)
assert aden.programmer_define() == 'Программист', 'Ошибка programmer_define()'
assert aden.age_define() == 'Молодой', 'Ошибка age_define()'
# Создайте столько экземпляров, сколько нужно,
# чтобы через разные assert проверить все методы во всех вариантах.
test_oldschool_programmer = Contact('Romero', 1967, True)
assert test_oldschool_programmer.programmer_define() == 'Программист', (
    'Ошибка programmer_define()'
)
assert test_oldschool_programmer.age_define() == 'Олдскул', (
    'Ошибка age_define()'
)
