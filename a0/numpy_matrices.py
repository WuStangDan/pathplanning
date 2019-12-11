# Matrices in numpy are very useful tools.
# First import the numpy package as np
import numpy as np

# First create an array of length 5 containing only zeros.
array = np.zeros([5])
print(array)
print('')

# Make the first element 10.
array[0] = 10

# Make the last element 5.
array[-1] = 5
print(array)
print('')

# Add 1 to all elements in the array.
array += 1
print(array)
print('')

# Now for Matrices.
# Create a matrix of 5 rows and 10 columns containing only zeros.
matrix = np.zeros([5,10])
print(matrix)
print('')

# Fill every element in the matrix with the value of its row multiplied by it's column.
for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        matrix[r,c] = r*c
print(matrix)
print('')


# Print the value in row 0, column 3 and row 2, column 3.
print(matrix[0,3])
print(matrix[2,3])
