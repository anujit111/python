# Remove empty tuples from a list
def remove_empty_tuples(lst):
    return [tup for tup in lst if tup]

# Test the function
input_list = [(), (1, 2), (), (3, 4), (), ()]
result = remove_empty_tuples(input_list)
print("List after removing empty tuples:", result)
