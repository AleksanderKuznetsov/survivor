"""
Сalculate distance by speed and travel time
"""


def odometer(oksana: list) -> int:
    """
    :param oksana: array, index from 0. Even - speed. Odd - travel time
    :return: Distance
    """
    distance = 0
    summa = 0
    for i, value in enumerate(oksana):
        if i == 1:
            summa = value * oksana[i-1]
            distance += summa
        elif i % 2 == 1:
            summa = (value - oksana[i-2]) * oksana[i-1]
            distance += summa

    return distance
