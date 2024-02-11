def split_and_join(string):
    words = string.split()
    return '-'.join(words)

# Test the function
string = "hello world"
print("After split and join:", split_and_join(string))
