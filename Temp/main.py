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

