
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

                 