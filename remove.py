def remove_duplicates(string):
    return ''.join(set(string))

# Test the function
string = "hello"
print("String after removing duplicates:", remove_duplicates(string))
