# Python | Get Kth Column of Matrix
def get_kth_column(matrix, k):
    return [row[k] for row in matrix]

# Test the function
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 1
column = get_kth_column(matrix, k)
print("Kth column of the matrix:", column)
