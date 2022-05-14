"""
How many days will the battalion fill the training ground.
Every day, each battalion occupies one cell horizontally and vertically.
Naming by assignment.
"""


def ConquestCampaign(N: int, M: int, L: int, battalion: list) -> int:
    """
    :param N: 1 polygon size
    :param M: 2 polygon size
    :param L: How many areas drop off
    :param battalion: Landing coordinates: even - N, odd - M
    :return: Days of landfill filling
    """
    day = 1  # Disembarkation is the first day.
    polygons = L

    # Form a polygon
    arr_a = []
    for i in range(N):
        arr_b = []
        for j in range(M):
            arr_b.append(0)
        arr_a.append(arr_b)

    # Paratroopers land
    for i in range(L):
        _STR = battalion[0] - 1
        _STL = battalion[1] - 1
        arr_a[_STR][_STL] = 1
        battalion.pop(0)
        battalion.pop(0)

    # Occupy perimeters.
    while polygons < N*M:
        for i in range(N):
            for j in range(M):
                if arr_a[i][j] == day:
                    if i < N-1 and arr_a[i + 1][j] == 0:
                        arr_a[i + 1][j] = day+1
                        polygons += 1
                    if i > 0 and arr_a[i - 1][j] == 0:
                        arr_a[i - 1][j] = day+1
                        polygons += 1
                    if j < M-1 and arr_a[i][j+1] == 0:
                        arr_a[i][j + 1] = day+1
                        polygons += 1
                    if j > 0 and arr_a[i][j-1] == 0:
                        arr_a[i][j - 1] = day+1
                        polygons += 1

        # Add a new day
        day += 1

    return day
