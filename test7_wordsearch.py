"""
Split text into lines by width and find the word
"""


def WordSearch(page_width: int, str_start: str, subs: str) -> list:
    """
    :param page_width: line width
    :param str_start: original string
    :param subs: search word
    :return: list of strings where 1 = search match
    """
    # Split the string by space. Get an array.
    array_start = str_start.split()
    array_stl = []  # Intermediate array. Matrix column.
    array_str = []  # Intermediate array. Matrix row.
    array_end = []  # Final array.
    symbols = 0  # Number of characters in the words of the string.
    iteration = 0  # Number of loop iterations.

    for word in array_start:
        len_word = len(word)
        iteration += 1
        # Word is longer than line width and word is first.
        if len_word > page_width and symbols == 0 and len(array_start) - iteration != 0:
            # Split the word.
            s1 = word[:page_width - len_word]
            s2 = word[page_width - len_word:]
            array_stl.append(s1)
            array_str.append(array_stl)
            array_stl = []  # Zero out the array.
            array_stl.append(s2)
            symbols = len(s2) + 1

        if len_word > page_width and symbols == 0 and len(array_start) - iteration == 0:
            # Split the word.
            s1 = word[:page_width - len_word]
            s2 = word[page_width - len_word:]
            array_stl.append(s1)
            array_str.append(array_stl)
            array_stl = []  # Zero out the array.
            array_stl.append(s2)
            array_str.append(array_stl)


        # The word is longer than the line width and the word is NOT the first.
        elif len_word > page_width and symbols > 0:
            array_str.append(array_stl)
            array_stl = []  # Zero out the array.
            # Split the word.
            s1 = word[:page_width - len_word]
            s2 = word[page_width - len_word:]
            array_stl.append(s1)
            array_str.append(array_stl)
            array_stl = []  # Zero out the array.
            array_stl.append(s2)
            symbols = len(s2) + 1

        #  Current word + length of previous < page width. The word is NOT the last
        elif len_word + symbols <= page_width and len(array_start) - iteration != 0:
            array_stl.append(word)
            symbols += len_word + 1

        #  Current word + length of previous < page width. The word is the last
        elif len_word + symbols <= page_width and len(array_start) - iteration == 0:
            array_stl.append(word)
            array_str.append(array_stl)

        #  Current word + length of words in this line > page width. The word is NOT the last.
        elif len_word + 1 + symbols > page_width and len(array_start) - iteration != 0:
            array_str.append(array_stl)
            symbols = len_word + 1
            array_stl = [] # Zero out the array.
            array_stl.append(word)

        #  Current word + length of words in this line > page width. The word is the last.
        elif len_word + 1 + symbols > page_width and len(array_start) - iteration == 0:
            array_str.append(array_stl)
            array_stl = [] # Zero out the array.
            array_stl.append(word)
            array_str.append(array_stl)

    # Looking for substring matches.
    for line in array_str:
        number = 0
        for element in line:
            if subs == element:
                number += 1
        array_end.append(number)

    return array_end
