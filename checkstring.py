import re

def contains_special_character(string):
    return bool(re.search('[^A-Za-z0-9]', string))

# Test the function
string = "hello@123"
print("Contains special character:", contains_special_character(string))
