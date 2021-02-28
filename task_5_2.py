num = int(input("Введите целое число: "))
sum = 0
mult = 1
while (num != 0):
    sum = sum + num % 10
    mult = mult * (num % 10)
    num = num // 10
print("Сумма цифр числа равна: ", sum)
print("Произведение цифр равно: ", mult)

