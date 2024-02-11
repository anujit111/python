# Program to check if a number is an Armstrong number
num = int(input("Enter a number: "))
order = len(str(num))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if num == sum:
    print("{} is an Armstrong number.".format(num))
else:
    print("{} is not an Armstrong number.".format(num))
