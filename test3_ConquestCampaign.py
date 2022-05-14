"""
How many days will the battalion fill the training ground.
Every day, each battalion occupies one cell horizontally and vertically.
Naming by assignment.
"""


def ConquestCampaign(N: int, M: int, L: int, battalion: list) -> int:
    """
    :param N: сторона 1 полигона
    :param M: сторона 2 полигона
    :param L: на сколько полей высаживаются изначально
    :param battalion: массив с координатами высадки, где четные - по оси N, нечетные - M
    :return: сколько дней нужно для покрытия всего полигона
    """
    day = 1  # День высадки - день №1
    polygons = L

    # Сформируем полигон. Заполняем нулями
    arr_a = []
    for i in range(N):
        arr_b = []
        for j in range(M):
            arr_b.append(0)
        arr_a.append(arr_b)

    # Высаживаем спецназ
    for i in range(L):  # 1-й и 2-й элемент массива добавляем в полигон.
        _STR = battalion[0] - 1
        _STL = battalion[1] - 1
        arr_a[_STR][_STL] = 1  # Заполняем единицами места высадки.
        battalion.pop(0)  # Удаляем добавленные элементы.
        battalion.pop(0)

    # Занимаем территории
    while polygons < N*M:  # Цикл будет работать, пока не заполнится весь полигон >0
        for i in range(N):
            for j in range(M):
                # Элемент полигона содержит номер дня (т.е. отличное от нуля).
                if arr_a[i][j] == day:
                    # Ряд не последний и ниже ячейка не заполнена.
                    if i < N-1 and arr_a[i + 1][j] == 0:
                        arr_a[i + 1][j] = day+1  # Вносим день + 1 в ячейку ниже.
                        polygons += 1  # Увеличиваем заполненное поле на 1.
                    # Ряд не первый и выше ячейка не заполнена.
                    if i > 0 and arr_a[i - 1][j] == 0:
                        arr_a[i - 1][j] = day+1  # Вносим день + 1 в ячейку выше.
                        polygons += 1
                    # Тоже самое по ширине полигона.
                    if j < M-1 and arr_a[i][j+1] == 0:
                        arr_a[i][j + 1] = day+1  # Вносим день + 1 в ячейку справа.
                        polygons += 1
                    if j > 0 and arr_a[i][j-1] == 0:
                        arr_a[i][j - 1] = day+1  # Вносим день + 1 в ячейку слева.
                        polygons += 1

        # Добавляем день
        day += 1

    return day
