def replace_multiple_words(string, words, replacement):
    for word in words:
        string = string.replace(word, replacement)
    return string

# Test the function
string = "hello world, hello python"
words_to_replace = ["hello", "world"]
replacement = "K"
print("After replacement:", replace_multiple_words(string, words_to_replace, replacement))
