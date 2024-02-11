def remove_ith_character(string, i):
    return string[:i] + string[i+1:]

# Test the function
string = "hello"
i = 2
print("String after removal:", remove_ith_character(string, i))
