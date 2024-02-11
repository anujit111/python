def replace_all_occurrences(string, sub_string, replacement):
    return string.replace(sub_string, replacement)

# Test the function
string = "hello world, hello python"
sub_string = "hello"
replacement = "hi"
print("After replacement:", replace_all_occurrences(string, sub_string, replacement))
