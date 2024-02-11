def reverse_words(s):
    return ' '.join(s.split()[::-1])

# Test the function
string = "hello world"
print("Reversed words:", reverse_words(string))
