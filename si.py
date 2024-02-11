# Program to calculate simple interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate (in percentage): "))
time = float(input("Enter time (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display the result
print("Simple Interest: {}".format(simple_interest))
