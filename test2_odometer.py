"""
Сalculate distance by speed and travel time
"""


def odometer(oksana: list) -> int:
    """
    :param oksana: array, index from 0. Even - speed. Odd - travel time
    :return: Distance
    """
    distance = 0
    for i, value in enumerate(oksana):
        if i % 2 == 0:
            distance += value

    return distance
