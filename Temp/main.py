
# a = 3
# b = 2
# c = 4
# if a * b > c and (c % a == 0 or c % b == 0):
#     print("yes")
# else:
#     print("no")   

# =================================================================

# n = int(input('Введите число дней: '))
# max_day = 0
# max_temp = 0

# for i in range(n):
#     x = int(input('Введите дневную температуру: '))
#     if (x > 0):
#         max_temp = max_temp + 1
#         if (max_temp > max_day):
#             max_day = max_temp
#     else:
#         max_temp = 0
# print(max_day)

# =================================================================

# coins = [0, 1, 1, 1, 1, 0]
# min0 = 0
# min1 = 0

# for i in range(0, len(coins)):
#     if (coins[i] == 0):
#         min0 += 1
#     else:
#         min1 += 1
# if (min0 <= min1):
#     print(min0)
# else:
#     print(min1)    

# =================================================================

# s = 13 # summa chisel x, y
# p = 40 # proizvedenie chisel x, y

# d = s**2 - (4*-1*-p)
# x = int((-s - d**(0.5)) / (-1 * 2))
# y = int((-s + d**(0.5)) / (-1 * 2))

# if (x <= y):
#     print(x, y)
# else:
#     print(y, x)    

# =================================================================

# n = 3
# nTemp = 1

# while nTemp <= n:
#     print(nTemp)
#     nTemp = nTemp * 2
# # ili
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1

# =================================================================

# list_1 = [1, 12, 6, 7, 8, 15]
# k = 11

# near = list_1[0]
# temp = abs(list_1[0] - k) # abs() модуль числа

# for i in range (len(list_1)):
#     if list_1[i] * k == k * k:
#         near = list_1[i]
#         break
#     else:
#         if abs(list_1[i] - k) < temp:
#             temp = abs(list_1[i] - k)
#             near = list_1[i]        
# print(near) 

# =================================================================

# k = 'ноутбук'
# tempK = k.upper()
# count = 0
# eng = [{"AEIOULNSTRАВЕИНОРСТ": 1}, {"DGДКЛМПУ": 2}, {"BCMPБГЁЬЯ": 3}, {"FHVWYЙЫ": 4}, {"KЖЗХЦЧ": 5}, {"JXШЭЮ": 8}, {"QZФЩЪ": 10}]
# # ru = tuple({1: "АВЕИНОРСТ"},{2: "ДКЛМПУ"}, {3: "БГЁЬЯ"}, {4: "ЙЫ"}, {5: "ЖЗХЦЧ"}, {8: "ШЭЮ"}, {10: "ФЩЪ"})

# for i in tempK:
#     for dict in eng:
#         # print(dict)
#         for value in dict:
#             # print(value)
#             for j in value:
#                 if j == i:
#                     count += dict.get(value)
# print(count)   

# =================================================================

# var1 = '5 4' 
# var2 = '1 3 5 7 9' 
# var3 = '2 3 4 5'
# x = var2.split()
# y = var3.split()
# varTemp = set()
# for i in x:
#     for j in y:
#         if j == i:
#             varTemp.add(j)
# varEnd = list(sorted(varTemp))
# print(*varEnd)            

# =================================================================

# arr = [5, 8, 6, 4, 9, 2, 7, 3]
# countMax = 0
# count = 0
# for i in range (len(arr)):
#     if i == 0:
#         count = arr[len(arr) - 1] + arr[i] + arr[i + 1]
#     elif i == len(arr) - 1:
#         count = arr[i - 1] + arr[i] + arr[0]
#     else:    
#         count = arr[i-1] + arr[i] + arr[i + 1]
#         if countMax < count:
#             countMax = count
# print(countMax)      

# =================================================================

# def sum(a, b):
#     if a > 0 and b > 0:
#         count = sum(a-1, b-1) + 1 + 1
#         return count
#     elif a > 0 or b > 0:
#         count = sum(a-1, b-1) + 1
#         return count
#     else:
#         return 0

# a = 2
# b = 2
# print(sum(a, b))

 # =================================================================


# list1 = [1,2,3,5,8,15,23,38]
# list2 = list()
# temp = 0
# for i in list1:
#     if i % 2 == 0:
#         list2.append((i,i**2))
# print(list2)        

 # =================================================================

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def find_farthest_orbit(list_of_orbits):
#     orb = [(3.14*x*y) for x,y in list_of_orbits if x != y]
#     return orb.index(max(orb))
    
# print(orbits[find_farthest_orbit(orbits)])

# =================================================================

# stroka = 'как ве-тер сме-ёт лис-ти'

# def vinni (str = ' '):
#     dict = ["а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы"]
#     str = str.lower()
#     newStr = ""
#     for i in str:
#         for j in dict:
#             if i == j:
#                 newStr +=i
#             if i == " ":
#                 newStr += " "    
#     temp = newStr.split()
#     if len(temp) < 2:
#         print("Количество фраз должно быть больше одной!")
#     else:    
#         count = len(temp[0])
#         for k in temp:
#           if len(k) != count:
#             count+=1
#         if count == len(temp[0]):
#             print("Парам пам-пам")
#         else:
#             print("Пам парам")        
    
# vinni(stroka)

# =================================================================

# def print_operation_table(operation, num_rows=9, num_columns=9):
#         if num_rows < 2:
#           print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#         else:
#           for x in range(1, num_rows + 1):
#                 list_temp = list()
#                 for y in range (1, num_columns +1):
#                     list_temp.append(operation(x,y))
#                 print(*list_temp)

# print_operation_table(lambda x, y: x * y,)

# =================================================================

# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:                                         Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам        Парам пам-пам


# vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
# stroka = input("Введите строку: ").split()

# count_vowels = []
# print(stroka)
# for i in stroka:
#     count = len([x for x in i if x.lower() in vowels])
#     count_vowels.append(count)
# print(count_vowels)

# if count_vowels.count(count_vowels[0]) == len(count_vowels):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')



# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод:                                                           Вывод:
# print_operation_table(lambda x, y: x * y)                       1 2 3 4 5 6
#                                                                 2 4 6 8 10 12
#                                                                 3 6 9 12 15 18
#                                                                 4 8 12 16 20 24
#                                                                 5 10 15 20 25 30
#                                                                 6 12 18 24 30 36 

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     if num_rows < 2 or num_columns < 2:
#         print('error')
#     else:
#         print(' '.join(list(map(str, range(1, num_columns + 1)))))
#         for i in range(2, num_rows + 1):
#             print(i, end = ' ')
#             for j in range(2, num_columns + 1):
#                 print(operation(i, j), end=' ')
#             print()

# print_operation_table(lambda x, y: x * y) 