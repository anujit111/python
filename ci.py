# Program to calculate compound interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate (in percentage): "))
time = float(input("Enter time (in years): "))
n = float(input("Enter the number of times interest is compounded per year: "))

# Calculate compound interest
compound_interest = principal * (1 + rate / (100 * n))**(n * time) - principal

# Display the result
print("Compound Interest: {}".format(compound_interest))
