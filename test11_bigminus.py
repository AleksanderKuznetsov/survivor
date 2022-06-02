"""
Сompute the difference for any given parameters
"""


def BigMinus(line1: str, line2: str) -> str:
    """
    calculate in a column
    :param line1: first number in str
    :param line2: second number in str
    :return: difference in str
    """
    flag = False  # if -1 from the next number: True.
    array_ = []

    # Find a long line and make it line1.
    if len(line1) < len(line2):
        line1, line2 = line2, line1
    elif len(line1) == len(line2) and int(line2[0]) > int(line1[0]):
        line1, line2 = line2, line1

    # Adding "0" to the beginning of a short string.
    line2 = "0" * (len(line1) - len(line2)) + line2

    # Cycle through line1 from the end to the beginning.
    for i in range(len(line1)-1, -1, -1):
        if int(line1[i]) - int(line2[i]) < 0 and not flag:
            result = int(line1[i]) + 10 - int(line2[i])
            flag = True
        elif int(line1[i]) - int(line2[i]) <= 0 and flag:
            result = int(line1[i]) + 9 - int(line2[i])
        elif flag:
            result = int(line1[i]) - 1 - int(line2[i])
            flag = False
        else:
            result = int(line1[i]) - int(line2[i])
            flag = False
        array_.insert(0, str(result))

    return "".join(array_)
