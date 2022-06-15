"""
Checking if the second array is included in the first one (in two dimensions).
"""


def TankRush(str1: int, col1: int, map1: str, str2: int, col2: int, map2: str) -> bool:
    """
    :param str1: number of rows of the 1st array.
    :param col1: number of columns of the 1st array.
    :param map1: array1 in string with spaces.
    :param str2: number of rows of the 2nd array.
    :param col2: number of columns of the 2nd array.
    :param map2: array2 in string with spaces.
    :return: contains - True, not - False .
    """
    # Remove spaces from strings
    map1 = map1.replace(" ", "")
    map2 = map2.replace(" ", "")
    array1 = []
    array2 = []
    result = 0
    count = 0
    # Create array1
    count = 0
    last_col = 0
    last_str = 0
    for i in range(str1):
        temp = []
        for j in range(col1):
            temp.append(map1[count])
            count += 1
        array1.append(temp)

    # Create array2.
    count = 0
    for i in range(str2):
        temp = []
        for j in range(col2):
            temp.append(map2[count])
            count += 1
        array2.append(temp)

    count = 0
    # Looking for entry.
    for z in range(str1):  # Go through the rows of array1.
        for i in range(col1 - col2 + 1):  # Going through each column.
            temp = []
            for j in range(col2):
                temp.append(array1[z][i + j])  # Filling the temp array.
            for ii in range(str2):
                if temp == array2[ii] and count == 0:  # Temporary array equals array row 2.
                    count += 1
                    last_col = i
                    last_str = z
                    result += 1
                elif temp == array2[ii] and count > 0 and i == last_col and z - last_str == 1:
                    result += 1
                    last_col = i
                    last_str = z
                elif temp == array2[ii] and count > 0 and (i != last_col or z - last_str != 1):
                    count = 0

    if result >= str2:
        return True

    return False
