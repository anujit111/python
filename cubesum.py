def cube_sum(n):
    return ((n * (n + 1)) // 2) ** 2

# Get user input for the value of n
n = int(input("Enter the value of n: "))

# Calculate and print the cube sum
result = cube_sum(n)
print(f"The cube sum of first {n} natural numbers is: {result}")

