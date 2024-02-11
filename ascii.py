# Get user input for a character
character = input("Enter a character: ")

# Check if the input is a single character
if len(character) == 1:
    # Use ord() function to get the ASCII value
    ascii_value = ord(character)
    print(f"The ASCII value of '{character}' is: {ascii_value}")
else:
    print("Please enter a single character.")
