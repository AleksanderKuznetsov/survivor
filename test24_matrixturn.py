"""
Rotate a matrix
"""
# Function to rotate a matrix
def MatrixTurn(array_in: list, lines: int, columns: int,  count: int) -> list:
    """
        array_in : entry string
        lines: number of lines
        columns: number of columns
        count: number of matrix rotation steps
        top : start row index
        bottom : end row index
        left : start column index
        right : end column index
    """
    # Сonvert array to string
    array = []
    for line in array_in:
        array.append(list(line))

    for z in range(count):
        top = 0
        bottom = lines - 1

        left = 0
        right = columns - 1
        while left < right and top < bottom:

            # Save the first element of the next line,
            # this element will replace the first element current line
            prev = array[top + 1][left]

            # Move top row items one step to the right
            for i in range(left, right + 1):
                curr = array[top][i]
                array[top][i] = prev
                prev = curr

            top += 1

            # Move items in the rightmost column one step down
            for i in range(top, bottom + 1):
                curr = array[i][right]
                array[i][right] = prev
                prev = curr

            right -= 1

            # Move bottom row items one step to the left
            for i in range(right, left - 1, -1):
                curr = array[bottom][i]
                array[bottom][i] = prev
                prev = curr

            bottom -= 1

            # Move leftmost column items up one step
            for i in range(bottom, top - 1, -1):
                curr = array[i][left]
                array[i][left] = prev
                prev = curr

            left += 1

    # Return an array to a string
    array_in.clear()
    for i, line in enumerate(array):
        array_in.append(''.join(line))

    return array_in
