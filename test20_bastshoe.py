"""
Make a text editor.
"""


class NewLine:
    """
    Actions in a text editor. without encapsulation
    """
    def __init__(self, line=[], accumulation=[], result='', operations=[]):
        self.line = line  # Массив текущего состояние строки. Сюда добавляем/удаляем символы.
        self.accumulation = accumulation  # Массив состояний строк после каждого этапа.
        self.result = result  # Результат, который выводим после каждого шага (str).
        self.operations = operations  # Список операций.

    # В конец текущей строки добавить строку
    def s(self, text):
        """
        Проверяем условие добавляется ли строка после отмены.
        По заданию предыдущая цепочка операций для Undo обнуляется -
        (откатить можно только последнюю операцию 1 или 2).
        """
        if len(self.operations) > 1 and self.operations[-1] == "undo":
            # Сохранить в переменную последний элемент массива состояний.
            xxx = self.accumulation[-1]
            # Обнулить массивы.
            self.line.clear()
            self.accumulation.clear()
            self.operations.clear()
            # В массиве состояний оставить последний элемент.
            self.accumulation.append(xxx)
            # В массив текущего состояния добавить последний элемент.
            for i in self.accumulation:
                self.line.append(i)
        # Добавить элемент по заданию.
        for t in text:
            self.line.append(t)
        self.result = ''.join(self.line)
        self.accumulation.append(self.result)  # Добавить в массив состояний строк.
        self.operations.append("s")
        return self.result

    def n(self, count):
        """
        Удалить N символов из конца текущей строки.
        Если N больше длины текущей строки, удаляем из неё все символы.
        :param count: сколько символов удалить
        :return: текущее состояние строки
        """
        count = int(count)
        if len(self.operations) > 1 and self.operations[-1] == "undo":
            # Сохранить в переменную последний элемент массива состояний.
            xxx = self.accumulation[-1]
            # Обнулить массивы.
            self.accumulation.clear()
            self.operations.clear()
            # В массиве состояний оставить последний элемент.
            self.accumulation.append(xxx)
        for i in range(count):
            # Символов к удалению больше или равно, чем длина строки
            if count >= len(self.line) and i == 0:
                self.line.clear()
                self.accumulation.clear()
                self.result = ''.join(self.line)
                self.operations.append("n")
                return self.result
            self.line.pop()  # Удалить по одному
        self.result = ''.join(self.line)
        self.accumulation.append(self.result)  # Добавить в массив состояний строк.
        self.operations.append("n")
        return self.result

    def i(self, count):
        """
        Выдать i-й символ текущей строки.
        Если индекс за пределами строки, вернуть пустую строку
        :param count: Номер символа с 0
        :return: Текущее состояние строки
        """
        count = int(count)
        xx = list(''.join(self.line))
        if count + 1 > len(xx):
            self.line.clear()
            self.operations.append("i")
            return self.line
        self.operations.append("i")
        return xx[count]

    def undo(self):
        """
        Отменить последнее действие.
        :return: Текущее состояние строки
        """
        # Вначале отработать условие - если undo выполняется после обнуления.
        # Посчитать сколько добавлений "s" было.
        flag_s = 0
        for line in self.operations:
            if line == "s":
                flag_s += 1
        # Если было одно добавление, то не меняем местами элементы accumulation,
        # как это делать будем ниже. Взять предпоследний элемент.
        if flag_s == 1:
            self.result = self.accumulation[-2]
            return self.result

        count_undo = 0
        for i in range(len(self.operations)-1, 0, -1):
            if self.operations[i] == "undo":
                count_undo += 1
            else:
                break
        # Поменять местами первый и последний элемент - делаем сдвиг массива.
        # Вначале проверка, чтобы отмен было не больше, чем длина accumulation.
        if count_undo < len(self.accumulation) - 1:
            self.accumulation.insert(0, self.accumulation[-1])
            self.accumulation.pop(-1)
        # Взять последний элемент массива.
        self.result = self.accumulation[-1]
        self.operations.append("undo")
        self.line.clear()
        for i in self.result:
            self.line.append(i)
        return self.result

    def redo(self):
        """
        Вернуть последнюю отмену.
        :return: Текущее состояние строки.
        """
        undo_x = 0
        redo_x = 0
        # Посчитать сколько redo и undo. Чтобы не отменить отмену больше раз, чем было.
        # Чтобы не перекрутить массив при сдвиге.
        for i in range(len(self.operations)-1, 0, -1):
            if self.operations[i] == "redo":
                redo_x += 1
                continue
            elif self.operations[i] == "undo":
                undo_x += 1
            elif self.operations[i] != "undo":
                break
        # Поменять местами первый и последний элемент - делаем сдвиг массива.
        if redo_x < undo_x:
            self.accumulation.append(self.accumulation[0])
            self.accumulation.pop(0)
        self.result = self.accumulation[-1]
        self.operations.append("redo")
        self.line.clear()
        for i in self.result:
            self.line.append(i)
        return self.result

    def error(self):
        """
        Когда команда введена неверно.
        :return: Последнее значение строки.
        """
        return self.accumulation[-1]


def BastShoe(command: str):
    """
    :param command: Вводимая строка
    :return: Текущее состояние строки
    """
    # Создать объект класса
    example = NewLine()
    # Сделать из строки формата "1 Текст" массив, запятая по первому пробелу.
    command = command.split(" ", 1)
    if command[0] == '1':
        return example.s(command[1])

    elif command[0] == '2':
        return example.n(command[1])

    elif command[0] == '3':
        return example.i(command[1])

    elif command[0] == '4':
        return example.undo()

    elif command[0] == '5':
        return example.redo()

    else:
        return example.error()
