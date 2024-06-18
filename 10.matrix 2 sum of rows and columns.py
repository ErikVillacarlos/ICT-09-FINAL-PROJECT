
import numpy as np

# Define the matrix as a NumPy array
matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print('matrix:',matrix)
print()


# Calculate row sums
row_sums = np.sum(matrix, axis=1)

# Calculate column sums
col_sums = np.sum(matrix, axis=0)
print()

# Print sums
print("Row sums:", row_sums)
print()
print("Column sums:", col_sums)
