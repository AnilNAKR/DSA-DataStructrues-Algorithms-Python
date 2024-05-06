import numpy as np

twoDArray = np.array(
    [[11, 15, 10, 6], [10, 14, 111, 5], [12, 17, 12, 8], [15, 18, 14, 9]]
)
print(twoDArray)

# Insertion - Two Dimensional Array
# Adding Columns
# Adding Rows

# newTwoDArray = np.insert(twoDArray, 1, [[1, 2, 3, 4]], axis=0)
# print(newTwoDArray)

# newTwoDArray = np.append(twoDArray, [[1, 2, 3, 4]], axis=0)
# print(newTwoDArray)


# Accessing an element of Two Dimensional Array
# def accessElements(array, rowIndex, colIndex):
#     if rowIndex >= len(array) and colIndex >= len(array[0]):
#         print("Incorrect Index")
#     else:
#         print(array[rowIndex][colIndex])


# accessElements(twoDArray, 1, 2)


# # Array Traversal in Two Dimensional Array
# def traverseTDArrar(array):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             print(array[i][j])


# traverseTDArrar(twoDArray)


# Searching an element in Two Dimensioanl Array
# def searchTDArray(array, value):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             if array[i][j] == value:
#                 return (
#                     "The value "
#                     + str(value)
#                     + " is located at index "
#                     + str(i)
#                     + " "
#                     + str(j)
#                 )
#         return "The element is not found"


# print(searchTDArray(twoDArray, 15))


# # Deletion - Two Dimensional Array
# newTDArray = np.delete(twoDArray, 0, axis=1)
# print(newTDArray)

# Time and Space complexity in 2D Array

# When to use/avoid Arrays
