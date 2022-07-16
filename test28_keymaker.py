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
    # Add the array with closed doors.
    for key in range(k):
        array.append(1)

    for key in range(1, k + 1):
        if key == 2 or key == 3:
            array[key - 1] = 0
        # Regularity - after the fourth character, the alternation of 000 and 111.
        if key > 4 and 0 < (key - 4) % 6 <= 3:
            array[key - 1] = 0

    # Translate int→str.
    for key in range(k):
        array[key] = str(array[key])

    return ''.join(array)


def new_function(count: int) -> None:
    """
    Apply Keymaker function need number of times.
    :param count: How many keys.
    :return: str
    """
    for key in range(1, count+1):
        print(Keymaker(key), "//", key)
