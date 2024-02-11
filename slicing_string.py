def can_become_empty(string, target):
    while string:
        if string == target:
            return True
        string = string[:-1]  # Delete the last character
    return False

# Test the function
string = "abcde"
target = ""
print("Can become empty:", can_become_empty(string, target))
