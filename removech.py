# Method 1: Using string slicing
def remove_character(s, i):
    return s[:i] + s[i+1:]

# Test the function
string = "example"
index = 2
print("After removal:", remove_character(string, index))
