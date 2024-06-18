
def transpose_matrix(matrix):
    # Initialize a new matrix to store the transposed matrix
    transposed = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # Perform the transpose operation
    for i in range(3):
        for j in range(3):
            transposed[i][j] = matrix[j][i]

    return transposed

# Example 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Transpose the matrix
transposed_matrix = transpose_matrix(matrix)

# Print the transposed matrix
print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)
