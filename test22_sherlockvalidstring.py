"""
Selection of valid passwords.
"""


def SherlockValidString(text: str) -> bool:
    """
    In the password string, all letters occur the same
    the number of times is True.
    It is allowed to delete any one letter to fulfill the condition
    equality of the frequency of all letters.
    :param text: string with Latin characters.
    :return: True or False
    """
    dictionary = {}  # In this dictionary we will add up the count of the number of repetitions.
    dictionary2 = {}  # Add the number of values to this dictionary.
    # Form a dictionary with counting the number of repetitions.
    for i, item in enumerate(text):
        x = dictionary.get(item, 0)  # Get the key value. If not, 0.
        x += 1  # To the value of the key +1 (making a counter).
        dictionary[item] = x  # Add a pair to the dictionary. The value is a counter.

    # Form a dictionary. Count the number of values.
    for key, value in dictionary.items():
        x = dictionary2.get(value, 0)
        x += 1
        dictionary2[value] = x

    # Sort the dictionary in descending order of values.
    # The last value will be the one that you can try to reduce.
    # For example {1:3, 2:1}
    temp = dict(sorted(dictionary2.items(), key=lambda x: x[1], reverse=True))
    # Save keys and values to separate lists.
    key_list = list(temp.keys())
    value_list = list(temp.values())

    # If the list length = 1, then the number of repetitions is the same
    if len(key_list) == 1:
        return True
    # If the list length = 2 and the number of keys differs by 1,
    # in this case, the last element of the value = 1, means the removal of one
    # of the symbol will give True. {1:3, 2:1} means that 1 character is repeated 3 times,
    # and 2 characters - once. Therefore, we can delete 1 character and it will be True.
    if len(key_list) == 2 and abs(key_list[1] - key_list[0]) == 1 and value_list[1] == 1:
        return True

    # Otherwise, if dictionary2 has more than 2 keys, then the condition will not work.
    return False
