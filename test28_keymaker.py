"""
Write a program that simulates the operation of the Key Wizard.
"""
def Keymaker(k: int) -> str:
    """
    1. In the first step, he opens all the doors.
    2. On the second step, he closes every other door.
    3. In the third step, he checks every third door,
    opens it if it is closed, and closes it if it is open.
    4. At the n-th step, he thus "switches" every n-th door.
    :param k: Number of doors.
    :return: Door status bar.
    """
    array = []
    count = 1

    for key in range(1, k+1):
        if key == count**2:  # sequence of squares of natural numbers.
            array.append("1")
            count += 1
            continue
        array.append("0")

    return ''.join(array)


def new_function(count):
    """
    Apply Keymaker function need number of times.
    :param count: How many keys.
    :return: str
    """
    for key in range(count):
        print(Keymaker(key), "//", key)
