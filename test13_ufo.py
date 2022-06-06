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

    for dat in data:
        summa = 0
        value = list(str(dat))
        for j in range(count):
            summa += int(value[j])*num**(count-1-j)
        array.append(summa)

    return array
