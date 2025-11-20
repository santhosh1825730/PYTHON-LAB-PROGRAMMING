count = 1
sum = 0

while count <= 20:
    if count % 5 == 0:
        sum = sum + count
    count = count + 1

print("The Sum of Numbers from 1 to 20 divisible by 5 is:", sum)
