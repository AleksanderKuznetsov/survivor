"""
Сonvert octal and hexadecimal systems to decimal.
"""


def UFO(count: int, data: list, octal: bool) -> list:
    """
    :param count: number of numbers in each array iteration.
    :param data: input array
    :param octal: true - octal, false - hexadecimal.
    :return: array of decimal numbers.
    """
    array = []
    # Set number system.
    if octal:
        num = 8
    else:
        num = 16

    for dat in range(count):
        summa = 0
        value = list(str(data[dat]))
        lenn = len(value)
        for j in range(lenn):
            summa += int(value[j])*num**(lenn-1-j)
        array.append(summa)

    return array
