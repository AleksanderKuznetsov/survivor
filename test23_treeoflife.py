"""
Write a program that simulates N years of tree development.
"""


def TreeOfLife(lines: int, columns: int, years: int, array: list) -> list:
    """
    :param lines: matrix rows
    :param columns: matrix columns
    :param years: how many years to analyze
    :param array: incoming string
    :return: outgoing string
    """
    temp = []
    # Translate string to 2D array
    for i, arr in enumerate(array):
        temp.append(list(arr))

    # cycle for each year
    for x in range(years + 1):
        # Replace in year zero "+" and "." to numbers.
        for y in range(lines):
            for z in range(columns):
                if x == 0 and temp[y][z] == "+":
                    temp[y][z] = 1
                elif x == 0 and temp[y][z] == ".":
                    temp[y][z] = 0

                # Add year
                if x > 0:
                    temp[y][z] += 1

        # Process every year according to the rule: >= 3 - delete.
        for y in range(lines):
            for z in range(columns):
                # Even skip (actually odd)
                if x % 2 != 0:
                    break
                # Top left corner
                if z == 0 and y == 0 and temp[y][z] >= 3:
                    if temp[y+1][z] < 3:
                        temp[y+1][z] = 0
                    if temp[y][z+1] < 3:
                        temp[y][z+1] = 0
                    temp[y][z] = 0
                # Bottom right corner
                if z == columns-1 and y == lines-1 and temp[y][z] >= 3:
                    temp[y][z] = temp[y-1][z] = temp[y][z-1] = 0
                # Lower left corner
                if z == 0 and y == lines-1 and temp[y][z] >= 3:
                    if temp[y][z+1] < 3:
                        temp[y][z+1] = 0
                    temp[y][z] = temp[y-1][z] = 0
                # Top right corner
                if z == columns-1 and y == 0 and temp[y][z] >= 3:
                    if temp[y+1][z] < 3:
                        temp[y+1][z] = 0
                    temp[y][z] = temp[y][z-1] = 0
                # Bottom line
                if z != 0 and z != columns-1 and y == 0 and temp[y][z] >= 3:
                    if temp[y][z+1] < 3:
                        temp[y][z+1] = 0
                    if temp[y+1][z] < 3:
                        temp[y+1][z] = 0
                    temp[y][z] = temp[y][z-1] = 0
                # Top line
                if z != 0 and z != columns-1 and y == lines-1 and temp[y][z] >= 3:
                    if temp[y][z+1] < 3:
                        temp[y][z+1] = 0
                    temp[y][z] = temp[y-1][z] = temp[y][z-1] = 0
                # Left column
                if z == 0 and y != 0 and y != lines-1 and temp[y][z] >= 3:
                    if temp[y][z+1] < 3:
                        temp[y][z+1] = 0
                    if temp[y+1][z] < 3:
                        temp[y+1][z] = 0
                    temp[y][z] = temp[y-1][z] = 0
                # Right column
                if z == columns-1 and y != 0 and y != lines-1 and temp[y][z] >= 3:
                    if temp[y+1][z] < 3:
                        temp[y+1][z] = 0
                    temp[y][z] = temp[y-1][z] = temp[y][z-1] = 0
                # Middle.
                if temp[y][z] >= 3:
                    if temp[y][z+1] < 3:
                        temp[y][z+1] = 0
                    if temp[y+1][z] < 3:
                        temp[y+1][z] = 0
                    temp[y][z] = temp[y-1][z] = temp[y][z-1] = 0

    # Change numbers back to signs
    for y in range(lines):
        for z in range(columns):
            # Let's replace "+" and "." to numbers.
            if temp[y][z] == 0:
                temp[y][z] = "."
            else:
                temp[y][z] = "+"

    # Return an array to a string
    array.clear()
    for i, count in enumerate(temp):
        array.append(''.join(count))

    return array
