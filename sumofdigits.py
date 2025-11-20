num = int(input("Please Enter the number: "))
x = num
sum = 0
rem = 0

while num > 0:
    rem = num % 10
    num = num // 10
    sum = sum + rem

print("Sum of the digits of the entered number", x, "is =", sum)

