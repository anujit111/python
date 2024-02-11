from itertools import permutations

def permute_string(string):
    return [''.join(permutation) for permutation in permutations(string)]

# Test the function
string = "abc"
print("Permutations:", permute_string(string))
