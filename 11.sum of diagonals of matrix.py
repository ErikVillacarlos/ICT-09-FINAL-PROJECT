
matrix = [ [1, 2, 3],  [4, 5, 6],  [7, 8, 9]]
print('matrix:', matrix)
print()
# Initialize sum of diagonal elements
diagonal_sum = 0

# Iterate through the matrix
for i in range(len(matrix)):
    diagonal_sum += matrix[i][i]  # Sum the diagonal elements where row index equals column index

# Print the sum of diagonal elements
print("Sum of diagonal elements:", diagonal_sum)
