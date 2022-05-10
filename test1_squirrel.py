"""
Function - find the first digit of a factorial
"""


def squirrel(nuts: int) -> int:
    """
    :param nuts: non-negative integer
    :return: first digit of a factorial
    """
    # Factorial must start at 1.
    factorial = 1
    # Finding the factorial.
    for i in range(2, nuts+1):
        factorial *= i
    # Change integer to str type.
    type_str = str(factorial)

    return int(type_str[0])

