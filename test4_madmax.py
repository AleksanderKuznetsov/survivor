"""
The middle element of the array (odd number) must be equal to its largest number.
Everything on the left is in ascending order. Everything on the right - descending
"""


def MadMax(N: int, Tele: list) -> list:
    """
    :param N: array length (odd number)
    :param Tele: array (shuffled)
    :return: array by assignment
    """
    index = -1
    # Sorting the array.
    for i in range(N-1):
        for j in range(N-i-1):
            if Tele[j] > Tele[j+1]:
                Tele[j], Tele[j+1] = Tele[j+1], Tele[j]
    # Shaping impulse.
    for i in range(N-2):
        # If the middle of the array, swap the middle and last elements.
        if i == N / 2 + 0.5 - 1:
            Tele[i], Tele[N-1] = Tele[N-1], Tele[i]
        # If more than the middle - swap the elements.
        elif i > N / 2:
            Tele[i], Tele[N-1+index] = Tele[N-1+index], Tele[i]
            index -= 1

    return Tele
