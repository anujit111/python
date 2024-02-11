def fibonacci(n) :
    if n < 0:
        print('Invalid n')
        return
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a = 0 #previous element
        b = 1 #previous to previous element
        c = 0 #current element
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return c

n = int(input('Enter n : '))
result = fibonacci(n)
print(f'{n}-Fibonacci Number : {result}')