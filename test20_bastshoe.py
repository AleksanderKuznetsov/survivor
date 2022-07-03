"""
Text editor "Lapot"
"""


def BastShoe(command: str):
    """
     :param command: Input string
     :return: The current state of the row
    """
    def s(text):
        """
        Add text
        :param text: add text
        :return: str
        """
        global index, accumulation
        # Get line (look index).
        accum = accumulation[index]
        # Clean array after undo(index !=0)
        if index != 0:
            accumulation.clear()
            accumulation.append(accum)
        # Take array from line.
        accum = list(accum)
        # Add text one-by-one
        for t in text:
            accum.append(t)
        # Take line frm array
        accumulation.insert(0, ''.join(accum))
        # Zero index.
        index = 0
        result = accumulation[0]
        return result

    def n(count):
        """
        Del some letters
        :param count: count
        :return: line
        """
        global index, accumulation
        count = int(count)
        # Get line (look index).
        accum = accumulation[index]
        # Clean array after undo(index !=0)
        if index != 0:
            accumulation.clear()
            accumulation.append(accum)
        # Take array from line.
        accum = list(accum)
        for i in range(count):
            # More characters in the string than the length of the string.
            if count >= len(accumulation[0]) and i == 0:
                accumulation.insert(0, "")
                result = accumulation[0]
                index = 0
                return result
            # Delete one by one
            accum.pop()
        # Take line frm array
        accumulation.insert(0, ''.join(accum))
        result = accumulation[0]
        index = 0
        return result

    def i(count):
        """
        Print the i-th character of the current line
        """
        global index, accumulation
        count = int(count)
        last_element = list(accumulation[0])
        if count + 1 > len(last_element):
            result = ""
            index = 0
            return result
        index = 0
        return ''.join(accumulation[0][count])

    def undo():
        """
        Undo last action
        :return: line
        """
        global index, accumulation
        index += 1
        if index >= len(accumulation):
            result = accumulation[-1]
            index = len(accumulation) - 1
            return result
        result = accumulation[index]
        return result

    def redo():
        """
        Redo last action
        :return: line
        """
        global index, accumulation
        index -= 1
        if index <= 0:
            result = accumulation[0]
            index = 0
            return result
        result = accumulation[index]
        return result

    def error():
        """
        If the command is wrong
        """
        return accumulation[0]

    # Make an array from the "1 Text" format string, comma by first space.
    command = command.split(" ", 1)
    if command[0] == '1':
        return s(command[1])

    if command[0] == '2':
        return n(command[1])

    if command[0] == '3':
        return i(command[1])

    if command[0] == '4':
        return undo()

    if command[0] == '5':
        return redo()

    return error()


accumulation = [""]
index = 0
