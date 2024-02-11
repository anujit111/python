def is_symmetrical(s):
    return s == s[::-1]

# Test the function
string = "radar"
print("Is symmetrical:", is_symmetrical(string))
