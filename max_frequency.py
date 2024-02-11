from collections import Counter

def most_frequent_character(string):
    counts = Counter(string)
    return max(counts, key=counts.get)

# Test the function
string = "hello"
print("Most frequent character:", most_frequent_character(string))
