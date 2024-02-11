from collections import Counter

def word_frequency(string):
    return dict(Counter(string.split()))

# Test the function
string = "hello world hello"
print("Word frequency:", word_frequency(string))
