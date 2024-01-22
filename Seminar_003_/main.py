# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# 5 6 -> 2 3

# a = int(input('Введите число: '))
# b = int(input('Введите число: '))

# for i in range(1001):
#     for j in range(1001):
#         if i + j == a and i * j == b and i < j:
#             print(i, j)

# i + j = 5
# i * j = 6
            


# -------------------------------------------------------------------------------------------
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# list1 = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(list1)))

# -------------------------------------------------------------------------------------------------
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [3, 4, 5, 1, 2]

# list1 = [1, 2, 3, 4, 5] 
# k = 5
# k %= len(list1)
# res_list = list()

# # 1 2 3 4 5
# # 3 4 5 
# for i in range(k):
#     res_list.append(list1[len(list1) - k + i])
# print(res_list)

# # 3 4 5
# # 3 4 5 1 2
# for i in range(len(list1) - k):
#     res_list.append(list1[i])
# print(res_list)


# -------------------------------------------------------------------------------------------
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит


# list1 = [{"V": " S001"}, {"V": "S002 "}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":"S007"}]

# res_set = set()
# for dict in list1:
#     # print(set(dict.values()))
#     for key in dict:
#         res_set.add(dict[key].strip())
# print(res_set)



# -------------------------------------------------------------------------------------------------------------------
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

list1 = [0, -1, 5, 2, 3]
count = 0
for i in range(1, len(list1)):
    if list1[i - 1] < list1[i]:
        count += 1

print(count)