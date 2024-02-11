# Python – Vertical Concatenation in Matrix
def vertical_concatenate(matrix1, matrix2):
    return matrix1 + matrix2

# Test the function
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]
result = vertical_concatenate(matrix1, matrix2)
print("Concatenated matrix:")
for row in result:
    print(row)
