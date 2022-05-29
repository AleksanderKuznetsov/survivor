"""
Write a code to encrypt a text message and a decoder to decrypt it
"""
import math


def TheRabbitsFoot(line: str, encode: bool) -> str:
    """
    :param line: String to encode or decode
    :param encode: True - encode, False - decode
    :return: Encoded or decoded string
    """
    array_start = []  # Array to process string.
    array_finish = []  # Final array.

    # Encode == True.
    if encode:
        array_pre = []  # Intermediate array.
        letter_num = 0  # Letter number in a string.
        line = line.replace(" ", "")  # Remove spaces
        # Upper bound from the root of the string length.
        count_col = math.ceil(math.sqrt(len(line)))

        # Split a string into an array.
        for str_ in line:
            letter_num += 1
            array_pre.append(str_)
            if letter_num == count_col:
                array_start.append(array_pre)
                letter_num = 0
                array_pre = []
        array_start.append(array_pre)

    # Encode == False.
    if not encode:
        array_start = line.split()

    # Add a new array of letters vertically.
    for z in range(len(array_start)):
        for i in range(len(array_start)):
            for j in range(len(array_start[i])):
                if j == z:
                    array_finish.append(array_start[i][j])
        if encode and len(array_start) - z - 1 != 0:  # Add spaces, except the last.
            array_finish.append(" ")

    return "".join(array_finish)
