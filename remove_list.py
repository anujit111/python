# Remove empty lists from a list
def remove_empty_lists(lst):
    return [sublst for sublst in lst if sublst]

# Test the function
input_list = [[], [1, 2, 3], [], [4, 5], [], []]
result = remove_empty_lists(input_list)
print("List after removing empty lists:", result)
