def find_uncommon_words(string1, string2):
    words1 = set(string1.split())
    words2 = set(string2.split())
    return words1.symmetric_difference(words2)

# Test the function
string1 = "hello world"
string2 = "world python"
print("Uncommon words:", find_uncommon_words(string1, string2))
