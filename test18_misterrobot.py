"""
Take any three consecutive elements of the array,
and shift them in a circle to the left an arbitrary number of times.
Determine whether this operation can be used to turn the array into an ascending order
"""


def MisterRobot(count: int, data: list) -> bool:
    """
    :param count: array length
    :param data: array
    :return: can be sorted - True. Not - False
    """
    xchange = True
    circle = 1
    while circle > 0:
        circle = 0
        for i in range(count - 3):
            # Check every 3 characters.
            for number in range(3):
                # Sorted in ascending order.
                if data[i] < data[i + 1] < data[i + 2]:
                    xchange = True
                    break
                # Swap elements.
                data[i], data[i + 1], data[i + 2] = data[i + 1], data[i + 2], data[i]
                xchange = False
                circle += 1
            # If you haven’t sorted in 3 attempts, sorting will no longer work.
            if not xchange:
                return False

    return True
