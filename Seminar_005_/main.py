# # Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# # повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# # встречаются в обоих наборах.
# # Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# # элементов второго множества. Затем пользователь вводит сами элементы множеств.

# # 11 6
# # 2 4 6 8 10 12 10 8 6 4 2
# # 3 6 9 12 15 18
# # 6 12

# list1 = '2 4 6 8 10 12 10 8 6 4 2'.split()
# list2 = '3 6 9 12 15 18'.split()
# list1 = [int(i) for i in list1]
# list2 = [int(i) for i in list2]


# # set1 = set(list1) & set(list2)
# print(*sorted(set(list1) & set(list2)))


# ----------------------------------------------------------------------------------------------------
# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9

# n = int(input())
# list1 = [int(input()) for i in range(n)]

# arr_count = []
# for i in range(len(list1) - 1):
#     arr_count.append(list1[i - 1]  + list1[i] + list1[i + 1])
# arr_count.append(list1[0] + list1[-1] + list1[-2])

# print(max(arr_count))

# в цикле:
# -1 + 0 + 1 
# 0 + 1 + 2
# 1 + 2 + 3

# 0 1 2 3
# 1 2 3 4
    
# 0 + 1 + 2 ++
# 1 + 2 + 3 ++
# 2 + 3 + 0
# 3 + 0 + 1 -> -1 + 0 + 1 ++


# list1 = [1, 5, 98, 45, 12, 65]
# for i in list1:
#     print(i)

# for i in range(len(list1)):
#     print(list1[i])

# -------------------------------------------------------------------------------
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 9
# Output: 21
# Задание необходимо решать через рекурсию

# 0 1 2 3 4 5 6 7  8  9 10 11
# 0 1 1 2 3 5 8 13 21 34 55

# def f(n):
#     if n <= 1:
#         return 1
#     return f(n - 1) + f(n - 2)

# def rec(n):
#     return(f(n - 2))

# #                              f(5)
# #                 f(4)                    f(3)
# #         f(3)         f(2)           f(2)    f(1)    
# #     f(2)    f(1)  f(1)   f(0)   f(1)    f(0)
# # f(1)     f(0)
# # 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1

# n = int(input())
# print(rec(n))

# ------------------------------------------------------------------------------------
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# list1 = [1, 3, 3, 3, 4]
# maxx = max(list1)
# minn = min(list1)

# # for i in range(len(list1)):
# #     if list1[i] == maxx:
# #         list1[i] == min
# list1 = [minn if i == maxx else i for i in list1]
# print(list1)

# ----------------------------------------------------------------------------
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

# 17 -> 1 17 +
# 15 -> 1 3 5 15 - 
# 29 -> 1 29 + 
# 30 -> 1 2 3 5 6 10 15 30 -
# 21 -> 1 3 7 21

# def f(n):
#     for i in range(2, int(n ** 0.5 + 1)):
#         if n % i == 0:
#             return False
#     return True
# n = abs(int(input()))
# print(f(n))



# -------------------------------------------------------------
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def f(n):
#     if n == 0:
#         return
#     k = int(input('Введите число: '))
#     f(n - 1)
#     print(k, end = ' ')

# 1    
# f(n-1) -> 2
# +        f(n-1) -> 3
#            +      f(n-1) -> return
#                   +

def f(n):
    if n == 0:
        return ''
    k = int(input('Введите число: '))
    return f(n - 1) + f' {k}'

# 3 элемента
#         f(2) + ' 1'
#     f(1) + '2'
# f(0) + '3'
# ''
n = int(input('Введите кол-во: '))
print(f(n))


