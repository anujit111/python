def contains_all_vowels(string):
    vowels = set('aeiou')
    return vowels.issubset(set(string.lower()))

# Test the function
string = "Education is important"
print("Contains all vowels:", contains_all_vowels(string))
