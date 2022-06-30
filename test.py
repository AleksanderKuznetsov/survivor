# -- coding: utf-8 --ИЛИ
# def test(text):
#     dictionary = {}
#     for i in range(3):
#         dictionary[i] = text
#
#     return list(dictionary.keys())[-1]
#
# print(test('test'))


array = [1, 2, 3, 4]

array.append(array[0])
array.pop(0)

print(array)