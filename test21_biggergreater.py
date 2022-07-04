"""
Сonvert word by replacing characters
"""
from itertools import permutations


def BiggerGreater(text):
    """
    Receives as input a source string with a length of 2 or more Russian
     or English string (small) letters, and returns the final word.
    :param text: string
    :return: string
    """
    result_array = []
    # Find all combinations.
    for i in permutations(text):
        result_array.append(''.join(i))

    # Sorting the list.
    result_array.sort()

    # Looking for the next element after the match.
    for i in range(len(result_array)-1):
        if result_array[i] == text and result_array[i+1] != text:
            result = result_array[i + 1]
            return result

    return ""
