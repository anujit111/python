def is_binary_string(string):
    return all(char in '01' for char in string)

# Test the function
string = "101010"
print("Is binary string:", is_binary_string(string))
