def snake_to_pascal_case(string):
    return ''.join(word.capitalize() for word in string.split('_'))

# Test the function
snake_case_string = "hello_world"
print("Pascal case:", snake_to_pascal_case(snake_case_string))
