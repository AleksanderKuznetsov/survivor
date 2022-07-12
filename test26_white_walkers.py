"""
walker detection
"""


def white_walkers(village: str) -> bool:
    """
    :param village: incoming string.
    :return: are there walkers.
    """
    hodok = 0
    human1 = 0  # previous number of people.
    human2 = 0  # current number of people.
    flag = False
    for line in village:
        if line == "=":
            hodok += 1
            continue

        if line.isnumeric():
            human1 = human2
            human2 = int(line)

        if line.isnumeric() and human2 + human1 == 10 and hodok == 3:
            hodok = 0
            flag = True
            continue

        if line.isnumeric() and human2 + human1 != 10:
            hodok = 0

        if line.isnumeric() and human2 + human1 == 10 and hodok != 3:
            return False

    if not flag:
        return False

    return True
