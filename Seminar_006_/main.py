# def sum(a, b):
#     if b == 0:
#         return a
#     return sum(a + 1, b - 1)

# print(sum(5, 10))


# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:                     Вывод:
# 7                         3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

# n = int(input('Введите кол-во: '))
# list1 = []
# for i in range(n):
#     x = int(input('введите число: '))
#     list1.append(x)

# list1 = [int(input('введите число: ')) for i in range(int(input('Введите кол-во: ')))]
# print(list1)
# list2 = [int(input('введите число: ')) for i in range(int(input('Введите кол-во: ')))]
# print(list2)

# for el in list1:
#     if el not in list2:
#         print(el, end = ' ')



# -----------------------------------------------------------------------------------------------
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:                       Ввод:
# 5                           5
# 1 2 3 4 5                   1 5 1 5 1
# Вывод:                      Вывод:
# 0                           2

# 5
# 5 1 5 1 1
# -> 1

# 10 1 5 1 5 1

# list1 = [int(input('введите число: ')) for i in range(int(input('Введите кол-во: ')))]
# print(list1)

# count = 0
# for i in range(1, len(list1) - 1):
#     # if list1[i-1] < list1[i] and list1[i] > list1[i+1]:
#     if list1[i-1] < list1[i] > list1[i+1]:
#         count += 1
# print(count)
    


# ------------------------------------------------------------------------------------------------
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:           Вывод:
# 1 2 3 2 3       2
# 1 2 3 2 2       3

# list1 = [int(input('введите число: ')) for i in range(int(input('Введите кол-во: ')))]
# print(list1)

# count = 0
# for i in range(len(list1) - 1):
#     for j in range(i + 1, len(list1)):
#         if list1[i] == list1[j]:
#             count += 1
# print(count)

# 0 1 2 3 4
# 1 2 3 2 3

# i = 0
# j = 1 .. 4
# i = 1
# j = 2 .. 4
# i = 2
# j = 3 .. 4

# print(list(range(5)))

# ---------------------------------------------------------------------------------------------------
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. 
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:         Вывод:
# 300           220 284

# 220 -> 284
# 284 -> 220
# -> 220 284

# (0, 0), (1, 1), (2, 1), (3, 1), (4, 3), ...... (220, 284)

def sum_del(x):
    summa = 0
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            summa += i
    return summa

k = int(input('введите число: '))
for i in range(k):
    el1 = sum_del(i) # i = 220 -> el1 = 284
    el2 = sum_del(el1) # el1 = 284 -> el2 = 220
    if i < el1 and i == el2:
        print(el1, el2)