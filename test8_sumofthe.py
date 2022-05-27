"""
find a number from the list - the sum of the remaining numbers
"""


def SumOfThe(numbers: int, data: list) -> int:
    """
    :param numbers: summary length
    :param data: array of numbers
    :return: a number from the array equal to the sum of the other numbers
    """
    for i in range(numbers):
        summa = 0
        for j in range(numbers):
            summa += data[j]
        if data[i] == summa - data[i]:
            result = data[i]

    return result
