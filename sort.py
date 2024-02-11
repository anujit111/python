# Sort the values of first list using second list
def sort_list_by_other_list(lst1, lst2):
    return [x for _, x in sorted(zip(lst2, lst1))]

# Test the function
list1 = [10, 7, 8, 9, 1]
list2 = [1, 2, 3, 4, 5]
sorted_list1 = sort_list_by_other_list(list1, list2)
print("List 1 sorted by List 2:", sorted_list1)
