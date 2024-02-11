# Program to print duplicates from a list of integers
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

# Test the function
my_list = [1, 2, 3, 4, 2, 5, 6, 3]
duplicate_numbers = find_duplicates(my_list)
print("Duplicate numbers in the list:", duplicate_numbers)
