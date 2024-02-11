def count_matching_characters(string1, string2):
    return sum(1 for char1, char2 in zip(string1, string2) if char1 == char2)

# Test the function
string1 = "hello"
string2 = "hollow"
print("Number of matching characters:", count_matching_characters(string1, string2))
