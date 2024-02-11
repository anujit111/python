# Break a list into chunks of size N in Python
def chunk_list(lst, chunk_size):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

# Test the function
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 3
chunks = chunk_list(my_list, chunk_size)
print("List broken into chunks of size", chunk_size, ":", chunks)
