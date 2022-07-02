"""
Make a text editor.
"""


class NewLine:
    """
    Actions in a text editor. without encapsulation
    """
    def __init__(self, line=[], accumulation=[], result='', operations=[], delete = []):
        self.line = line  # Array of the current row state. Add/remove characters here.
        self.accumulation = accumulation  # Array of row states after each step.
        self.result = result  # The result that we print after each step (str).
        self.operations = operations  # List of operations.
        self.delete = delete

    # В конец текущей строки добавить строку
    def s(self, text):
        """
         Whether we check a condition the line is added after cancellation.
         By assignment, the previous chain of operations for Undo is reset to zero -
         (only the last operation 1 or 2 can be rolled back).
        """
        if len(self.operations) > 1 and self.operations[-1] == "undo":
            # Save the last element of the state array to a variable.
            xxx = self.accumulation[-1]
            # Zero out arrays.
            self.line.clear()
            self.accumulation.clear()
            self.operations.clear()
            # Leave the last element in the state array.
            self.accumulation.append(xxx)
            # Add the last element to the current state array.
            for i in self.accumulation:
                self.line.append(i)
        # Add item by assignment.
        for t in text:
            self.line.append(t)
        self.result = ''.join(self.line)
        self.accumulation.append(self.result)  # Add to row state array.
        self.operations.append("s")
        return self.result

    def n(self, count):
        """
         Remove N characters from the end of the current line.
         If N is greater than the length of the current string, remove all characters from it.
         :param count: how many characters to remove
         :return: the current state of the row
        """
        count = int(count)
        if len(self.operations) > 1 and self.operations[-1] == "undo":
            # Save the last element of the state array to a variable.
            xxx = self.accumulation[-1]
            # Zero out arrays.
            self.accumulation.clear()
            self.operations.clear()
            # Leave the last element in the state array.
            self.accumulation.append(xxx)
        for i in range(count):
            # The characters to be removed are greater than or equal to the length of the string
            if count >= len(self.line) and i == 0:
                self.line.clear()
                self.accumulation.clear()
                self.result = ''.join(self.line)
                self.operations.append("n")
                return self.result
            self.line.pop()  # Delete one by one
        self.result = ''.join(self.line)
        self.accumulation.append(self.result)  # Add to row state array.
        self.operations.append("n")
        return self.result

    def i(self, count):
        """
         Print the i-th character of the current line.
         If index is outside of string, return empty string
         :param count: Character number since 0
         :return: The current state of the row
        """
        count = int(count)
        xx = list(''.join(self.line))
        if count + 1 > len(xx):
            self.line.clear()
            self.operations.append("i")
            return ''.join(self.line)
        self.operations.append("i")
        return ''.join(xx[count])

    def undo(self):
        """
         Undo the last action.
         :return: The current state of the row
        """
        # Вначале отработать условие - если undo выполняется после обнуления.
        # Посчитать сколько добавлений "s" и "n" было.
        flag_s = 0
        for line in self.operations:
            if line == "s" or line == "n":
                flag_s += 1
        # If there was one addition, then do not swap the accumulation elements,
        # how to do it will be below. Take the penultimate element.
        # This is necessary so as not to erase all the lines when canceling multiple times.
        if flag_s == 1 and len(self.accumulation) == 2:
            self.result = self.accumulation[-2]
            return self.result

        if flag_s == 1 and len(self.accumulation) == 1:
            self.result = ""
            self.delete.append(self.accumulation[-1])
            self.accumulation.clear()
            self.line.clear()
            self.operations.clear()
            return self.result

        count_undo = 0
        for i in range(len(self.operations)-1, 0, -1):
            if self.operations[i] == "undo":
                count_undo += 1
            else:
                break
        # Swap the first and last element - we shift the array.
        # First check that there are no more undos than the length of accumulations.
        if count_undo < len(self.accumulation) - 1:
            self.accumulation.insert(0, self.accumulation[-1])
            self.accumulation.pop(-1)
        elif count_undo >= len(self.accumulation) - 1 and flag_s != 2:
            self.result = ""
            self.operations.append("undo")
            return self.result
            # Взять последний элемент массива.
        self.result = self.accumulation[-1]
        self.operations.append("undo")
        self.line.clear()
        for i in self.result:
            self.line.append(i)
        return self.result

    def redo(self):
        """
         Redo last undo.
         :return: The current state of the row.
        """
        if self.accumulation == []:
            result = self.delete[-1]
            return result
        undo_x = 0
        redo_x = 0
        # Calculate how many redo and undo. In order not to cancel the cancellation more times than it was.
        # In order not to twist the array when shifting.
        for i in range(len(self.operations)-1, 0, -1):
            if self.operations[i] == "redo":
                redo_x += 1
                continue
            if self.operations[i] == "undo":
                undo_x += 1
            if self.operations[i] != "undo":
                break
        # Swap the first and last element - we shift the array.
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
         When the command is entered incorrectly.
         :return: The last value of the string.
        """
        return self.accumulation[-1]


def BastShoe(command: str):
    """
     :param command: Input string
     :return: The current state of the row
    """
    # Create class object
    example = NewLine()
    # Make an array from the "1 Text" format string, comma by first space.
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

    return example.error()
