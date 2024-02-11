# Program to find the n-th Fibonacci number
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

n = int(input("Enter the value of n: "))
result = fibonacci(n)
print("The {}-th Fibonacci number is: {}".format(n, result))
