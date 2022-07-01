"""
Тесты задания 20 (текстовый редактор Лапоть)
"""

import unittest
from test20_bastshoe import BastShoe


def make_str(count):
    """
    Функция для создания строк. В строку записываю индекс цикла
    :param count: сколько строк добавить.
    :return: строки
    """
    result = ""
    for i in range(count):
        result = BastShoe("1 " + str(i))
    return result


class TestWork(unittest.TestCase):
    """
    Testing class
    """
    def test_s(self):
        """
        Добавить заданное количество строк
        """
        result = make_str(5)
        self.assertTrue(result == "01234")

    def test_n(self):
        """
        Удалить одну строку
        """
        make_str(5)
        result = BastShoe("2 1")
        self.assertTrue(result == "0123")

    def test_one_undo(self):
        """
        Отменить одно действие
        """
        make_str(5)
        result = BastShoe("4")
        self.assertTrue(result == "0123")

    def test_some_undo(self):
        """
        Отменить действий больше, чем строк.
        Результат ожидаем - должна остаться первая строка.
        """
        result = ""
        make_str(5)
        for undo in range(20):
            result = BastShoe("4")
        self.assertTrue(result == "0")

    def test_s_undo_s_undo(self):
        """
        Добавить строку после отмены и сделать множество отмен:
        Добавим строки → отменим одно действие → добавим одну строку → множество отмен.
        Ожидаем результат: должна быть строка перед добавлением.
        """
        result = ""
        make_str(5)  # Результат "01234"
        BastShoe("4")  # Результат "0123"
        make_str(1)  # Результат "01230"
        for undo in range(20):
            result = BastShoe("4")  # Результат "0123"
        self.assertTrue(result == "0123")

    def test_redo(self):
        """
        Тестирую Redo. Количество раз большее, чем Undo.
        """
        result = ""
        make_str(5)  # Результат "01234"
        BastShoe("4")  # Результат "0123"
        BastShoe("4")  # Результат "012"
        for undo in range(20):
            result = BastShoe("5")  # Результат "01234"
        self.assertTrue(result == "01234")

    def test_n_more_count(self):
        """
        Если удалить нужно больше символов, чем длина строки
        """
        make_str(5)  # Результат "01234"
        result = BastShoe("2 100")  # Результат ""
        self.assertTrue(result == "")

    def test_i_in(self):
        """
        Вернуть символ в рамках строки
        """
        make_str(5)
        result = BastShoe("3 3")  # Результат "2"
        self.assertTrue(result == "")

    def test_i_out(self):
        """
        Вернуть символ вне диапазона
        """
        make_str(5)
        result = BastShoe("3 100")  # Результат ""
        self.assertTrue(result == "")

    def test_error(self):
        """
        Если ошибочная команда
        """
        make_str(5)
        result = BastShoe("100 100")  # Результат "01234"
        self.assertTrue(result == "01234")

    def test_big_s_big_undo(self):
        """
        Много строк добавить, но убрать больше.
        Ожидаю в результате - первый символ
        """
        result = ""
        make_str(1000)
        for undo in range(1005):
            result = BastShoe("4")  # Результат "0"
        self.assertTrue(result == "0")

    def test_task(self):
        """
        Повторяю алгоритм задания.
        """
        make_str(3)  # Результат "012"
        BastShoe("2 2")  # Результат "0"
        BastShoe("4")  # Результат "012"
        BastShoe("4")  # Результат "01"
        BastShoe("1 *")  # Результат "01*"
        BastShoe("4")  # Результат "01"
        BastShoe("4")  # Результат "01"
        BastShoe("4")  # Результат "01"
        BastShoe("3 1")  # Результат "1"
        BastShoe("2 100")  # Результат ""
        make_str(3)  # Результат "012"
        BastShoe("4")  # Результат "01"
        BastShoe("4")  # Результат "0"
        BastShoe("5")  # Результат "01"
        BastShoe("5")  # Результат "012"
        BastShoe("5")  # Результат "012"
        BastShoe("4")  # Результат "01"
        BastShoe("2 1")  # Результат "0"
        BastShoe("4")  # Результат "01"
        BastShoe("5")  # Результат "0"
        BastShoe("5")  # Результат "0"
        result = BastShoe("5")  # Результат "0"
        self.assertTrue(result == "0")


if __name__ == '__main__':
    unittest.main()
