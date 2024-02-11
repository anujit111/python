import re

def contains_url(string):
    return bool(re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string))

# Test the function
string = "Visit our website at https://example.com"
print("Contains URL:", contains_url(string))
