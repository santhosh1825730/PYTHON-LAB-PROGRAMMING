num = int(input("Please Enter the number: "))
x = num
rev = 0

while num > 0:
    rem = num % 10
    num = num // 10
    rev = rev * 10 + rem

print("Reverse of the entered number", x, "is =", rev)

