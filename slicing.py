def rotate_string(string, n):
    return string[n:] + string[:n]

# Test the function
string = "hello"
n = 2
print("Rotated string:", rotate_string(string, n))
