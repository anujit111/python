from collections import Counter

def find_duplicate_characters(string):
    counts = Counter(string)
    return [char for char, count in counts.items() if count > 1]

# Test the function
string = "hello"
print("Duplicate characters:", find_duplicate_characters(string))
