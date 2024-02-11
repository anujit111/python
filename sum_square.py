def sum_of_squares(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

# Get user input for the value of n
n = int(input("Enter the value of n: "))

# Calculate and print the sum of squares
result = sum_of_squares(n)
print(f"The sum of squares of first {n} natural numbers is: {result}")
