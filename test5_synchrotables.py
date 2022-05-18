"""
sorting list 2 according to the shuffled sorting of list 1 without changing list 1
"""


def SynchronizingTables(N: int, ids: list, salary: list) -> list:
    """
    :param N: the length of both lists
    :param ids: list 1 - keys that cannot be changed
    :param salary: list 2 - to be sorted
    :return: sorted list 2
    """

    for z in range(N):
        for i in range(N):
            for j in range(N):
                if ids[i] > ids[j] and salary[i] < salary[j]:
                    salary[i], salary[j] = salary[j], salary[i]
                elif ids[i] < ids[j] and salary[i] > salary[j]:
                    salary[i], salary[j] = salary[j], salary[i]
    return salary
