"""
Implement an algorithm for finding a key key and print true if it is even
"""


def S(A: list, N: int) -> list:
    """
    Function S(A) that returns a list B
    :param A: input array
    :param N: the number of digits in the array (I don’t use it, but I need it on assignment)
    :return: list
    """
    B = []
    for i in range(len(A)):
        for j in range(len(A) - i):
            k = i + j
            B.append(sorted(A[j:k+1], reverse=True)[0])

    return B


def TransformTransform(array: list, N: int) -> bool:
    """
    Double transform def S, sum of array numbers, True if result is an even number.
    :param array: input array
    :param N: the number of digits in the array (I don’t use it, but I need it on assignment)
    :return: True or False
    """

    result_sum = 0
    # Transformation 1.
    result_1 = S(array, N)
    # Transformation 2.
    result_2 = S(result_1, N)

    # Sum of array numbers.
    for count in result_2:
        result_sum += count

    if result_sum % 2 == 0:
        return True

    return False
