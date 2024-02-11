def find_long_words(string, k):
    return [word for word in string.split() if len(word) > k]

# Test the function
string = "hello world python program"
k = 5
print("Words longer than", k, "characters:", find_long_words(string, k))
