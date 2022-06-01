"""
Сompute the difference for any given parameters
"""


def BigMinus(line1: str, line2: str) -> str:
    """
    :param line1: first number in str
    :param line2: second number in str
    :return: difference in str
    """
    if int(line1) - int(line2) > 0:
        result = int(line1) - int(line2)
    else:
        result = int(line2) - int(line1)
    return str(result)


print(BigMinus("12345678912345678912341", "1"))
