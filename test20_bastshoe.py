class NewLine:
    def __init__(self, line=[], accumulation=[], result='', operations=[]):
        self.line = line
        self.accumulation = accumulation
        self.result = result
        self.operations = operations

    # В конец текущей строки добавить строку
    def s(self, text):
        if len(self.operations) > 1 and self.operations[-1] == "undo":
            self.line = self.line[-2]
        for t in text:
            self.line.append(t)
        self.result = ''.join(self.line)
        self.accumulation.append(self.result)  # Добавить в результирующий массив
        self.operations.append("s")
        return self.result

    # Удалить N символов из конца текущей строки.
    # Если N больше длины текущей строки, удаляем из неё все символы.
    def n(self, count):
        count = int(count)
        for i in range(count):
            # Символов к удалению больше или равно, чем длина строки
            if count >= len(self.line) and i == 0:
                self.line.clear()
                break
            self.line.pop()  # Удалить по одному
        self.result = ''.join(self.line)
        self.accumulation.append(self.result)  # Добавить в результирующий массив
        self.operations.append("n")
        return self.result

    # Выдать i-й символ текущей строки.
    # Если индекс за пределами строки, вернуть пустую строку
    def i(self, count):
        count = int(count)
        xx = list(''.join(self.line))
        if count + 1 > len(xx):
            self.line.clear()
            self.operations.append("i")
            return self.line
        self.operations.append("i")
        return xx[count]

    def undo(self):
        self.accumulation.insert(0, self.accumulation[-1])
        self.accumulation.pop(-1)
        self.result = self.accumulation[-1]
        self.operations.append("undo")
        self.line.clear()
        for i in self.result:
            self.line.append(i)
        return self.result

    def redo(self):
        undo_x = 0
        redo_x = 0
        for i in range(len(self.operations)-1, 0, -1):
            if self.operations[i] == "redo":
                redo_x += 1
                continue
            elif self.operations[i] == "undo":
                undo_x += 1
            elif self.operations[i] != "undo":
                break
        if redo_x < undo_x:
            self.accumulation.append(self.accumulation[0])
            self.accumulation.pop(0)
        self.result = self.accumulation[-1]
        self.operations.append("redo")
        self.line.clear()
        for i in self.result:
            self.line.append(i)
        return self.result




def BastShoe(command: str):
    example = NewLine()
    command = command.split(" ", 1)
    if command[0] == '1':
        return example.s(command[1])

    if command[0] == '2':
        return example.n(command[1])

    if command[0] == '3':
        return example.i(command[1])

    if command[0] == '4':
        return example.undo()

    if command[0] == '5':
        return example.redo()




