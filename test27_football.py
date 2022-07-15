"""
Check the ability to sort the array in ascending order using one of the two tricks once.
"""


def Football(array: list, N: int) -> bool:
    """
    :param array: input array.
    :param N: number of characters in the array.
    :return: if orderable - True.
    """
    # Copy of sorted array - reference.
    array_sort = sorted(array)
    # Temporary array.
    temp = []

    # Populate temporary array.
    for line in array:
        temp.append(line)

    # Option 1. Replacing two arbitrary elements.
    for i in range(N):
        if array_sort[i] != temp[i]:
            index = temp.index(array_sort[i])
            temp[i], temp[index] = temp[index], temp[i]
            break

    # Check sorting.
    for i in range(N):
        if array_sort[i] != temp[i]:
            break
        if i == N-1 and array_sort[i] == temp[i]:
            return True

    # Reset temp.
    temp.clear()

    # Option 2. Reverse the order of an arbitrary
    # sequential chain of elements in an array.
    start = 0  # The first sort element within the array.
    end = N-1  # The last sort element within the array.

    # Determine the first sort element within the array.
    for i in range(end):
        if array[i] < array[i+1]:
            start = i+1
            break

    # Determine the last sort element within an array.
    for i in range(end):
        if array[i] > array[i+1]:
            end = i+1

    # Sort the middle of the array. separate variable.
    sort_temp = sorted(array[start:end+1])

    zz = 0
    # Fill temp array with values
    # taking into account the sorted middle.
    for i in range(N):
        if i >= start and i <= end:
            temp.append(sort_temp[zz])
            zz += 1
            continue
        temp.append(array[i])

    # Check sorting.
    for i in range(N):
        if array_sort[i] != temp[i]:
            break
        if i == N-1 and array_sort[i] == temp[i]:
            return True

    return False
