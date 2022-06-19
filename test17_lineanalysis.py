"""
Сheck the validity of a string against a pattern
"""


def LineAnalysis(lines: str) -> bool:
    """
    :param lines: cursive line.
    :return: True (*..*..*)
             False (*.*..*)
    """
    count_new = 0
    count = 0
    diff = 0
    for i, line in enumerate(lines):
        if line == "*":
            count += 1
        if line == "*" and count == 2:
            count_old = count_new
            count_new = i
            diff = count_new - count_old
        elif line == "*" and count > 2:
            count_old = count_new
            count_new = i
            if count_new - count_old != diff:
                return False
            diff = count_new - count_old

    return True
