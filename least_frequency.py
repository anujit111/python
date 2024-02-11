from collections import Counter

def least_frequent_character(string):
    counts = Counter(string)
    return min(counts, key=counts.get)

# Test the function
string = "hello"
print("Least frequent character:", least_frequent_character(string))
