"""
Group sales by product names, placing in the resulting
a list of products sorted by number of sales.
If these quantities for some goods coincide,
product names should follow in lexicographical ascending order
"""


def ShopOLAP(N: int, array: list) -> list:
    """
    :param N: number of lines
    :param array: rows to group
    :return: array of processed strings
    """
    array_temp = []
    array_result = []
    # Convert to 2D array.
    for line in range(N):
        # Split an entry into an array by a space.
        arr = array[line].split()
        for i, rec in enumerate(arr):
            if i == 1:
                arr[i] = int(rec)  # Вторую часть сделать числом.
        array_temp.append(arr)

    # Remove duplicates.
    for i, rec in enumerate(array_temp):
        flag = False
        # Compare each element of the array.
        for j, sub_rec in enumerate(array_temp):
            # Element must not be compared to itself.
            if i == j:
                continue
            # We found matches - sum up the values.
            if rec[0] == sub_rec[0]:
                rec[1] += sub_rec[1]
            # Iterate over the resulting array.
            for z, res_rec in enumerate(array_result):
                # If the first element is already in the array, change the flag.
                if rec[0] in res_rec[0]:
                    flag = True
        # If the flag is not True, then there was no match. Add to array.
        # So we will not add repetitions.
        if not flag:
            array_result.append(array_temp[i])

    # Sort array: second descending, first ascending if matched.
    array_result.sort(key=lambda x: (-x[1], x[0]))

    # Return 2D array to strings.
    array = []
    for i, line in enumerate(array_result):
        # Cast second element to str.
        line[1] = str(line[1])
        # Cast array to str. Comma = space.
        array.append(' '.join(line))

    return array
