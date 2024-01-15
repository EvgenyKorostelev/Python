a = 3
b = 2
c = 4
if a * b > c and (c % a == 0 or c % b == 0):
    print("yes")
else:
    print("no")   

# =================================================================

n = int(input('Введите число дней: '))
max_day = 0
max_temp = 0

for i in range(n):
    x = int(input('Введите дневную температуру: '))
    if (x > 0):
        max_temp = max_temp + 1
        if (max_temp > max_day):
            max_day = max_temp
    else:
        max_temp = 0
print(max_day)