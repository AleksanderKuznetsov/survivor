"""
Return line length (Task Unlock mobile phones)
"""


def PatternUnlock(length: int, hits: list) -> str:
    """
    :param length: array length
    :param hits: character input sequence
    :return: line length - the sum of vertical, horizontal and diagonal steps, excluding zeros
    """
    # Create a keyboard (2D array).
    keyboard = [[6, 1, 9], [5, 2, 8], [4, 3, 7]]
    count = 0

    for value in range(length):
        for i in range(3):
            for j in range(3):
                # For the value of the first element of the line,
                #  store the X and Y coordinates.
                if value == 0 and hits[0] == keyboard[i][j]:
                    x_axis1, y_axis1 = i, j
                # Hits element value == keyboard element.
                elif hits[value] == keyboard[i][j]:
                    # Save X and Y coordinates separately.
                    x_axis2, y_axis2 = i, j
                    # Previous element is on the same line vertically or horizontally.
                    if x_axis2 == x_axis1 or y_axis2 == y_axis1:
                        count += 1
                    # If not - diagonally.
                    else:
                        count += 1.41421356
                    # Assign current coordinates as past.
                    x_axis1, y_axis1 = i, j

    return str(round(count * 100000)).replace('0', '')
