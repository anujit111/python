def is_palindrome(s):
    return s == s[::-1]

# Test the function
string = "radar"
print("Is palindrome:", is_palindrome(string))
