# Count occurrences of an element in a list
def count_occurrences(lst, element):
    return lst.count(element)

# Test the function
my_list = [1, 2, 3, 4, 2, 2, 5]
element_to_count = 2
occurrences = count_occurrences(my_list, element_to_count)
print("Occurrences of", element_to_count, "in the list:", occurrences)
