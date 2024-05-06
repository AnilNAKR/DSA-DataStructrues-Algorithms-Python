# # Question 1 - Missing Number
# mylist = [
#     1,
#     2,
#     3,
#     4,
#     5,
#     6,
#     7,
#     8,
#     9,
#     10,
#     12,
#     13,
#     14,
#     15,
#     16,
#     17,
#     18,
#     19,
#     20,
#     21,
#     22,
#     23,
#     24,
#     25,
#     26,
#     27,
#     28,
#     29,
#     30,
#     31,
#     32,
#     33,
#     34,
#     35,
#     36,
#     37,
#     38,
#     39,
#     40,
#     41,
#     42,
#     43,
#     44,
#     45,
#     46,
#     47,
#     48,
#     49,
#     50,
#     51,
#     52,
#     53,
#     54,
#     55,
#     56,
#     57,
#     58,
#     59,
#     60,
#     61,
#     62,
#     63,
#     64,
#     65,
#     66,
#     67,
#     68,
#     69,
#     70,
#     71,
#     72,
#     73,
#     74,
#     75,
#     76,
#     77,
#     78,
#     79,
#     80,
#     81,
#     82,
#     83,
#     84,
#     85,
#     86,
#     87,
#     88,
#     89,
#     90,
#     91,
#     92,
#     93,
#     94,
#     95,
#     96,
#     97,
#     98,
#     99,
#     100,
# ]


# def findMissing(list, n):
#     sum1 = n * (n + 1) / 2
#     sum2 = sum(list)
#     print(sum1 - sum2)


# findMissing(mylist, 100)

# Question 2
# Leetcode 1 - Two sum

# def findPairs(nums, target):
#     for i in range(len(nums) - 1):
#         for j in range(i + 1, len(nums)):
#             if nums[i] == nums[j]:
#                 continue
#             elif nums[i] + nums[j] == target:
#                 print(i, j)


# myList = [1, 2, 3, 2, 3, 4, 5, 6]
# findPairs(myList, 6)


# # Question 3 - How to check if an array contains a number in Python
# import numpy as np

# myArray = np.array(
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# )


# def findNumber(array, number):
#     for i in range(len(array)):
#         if array[i] == number:
#             print(i)


# findNumber(myArray, 13)

# # Question 4 - How to find maximum product of two integers in the array where all elements are positive

# import numpy as np

# myArray = np.array(
#     [1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]
# )


# def findMaxProduct(array):
#     maxProduct = 0
#     for i in range(len(array) - 1):
#         for j in range(i + 1, len(array)):
#             if array[i] * array[j] > maxProduct:
#                 maxProduct = array[i] * array[j]
#                 paris = str(array[i]) + "," + str(array[j])
#     print(paris)
#     print(maxProduct)


# findMaxProduct(myArray)


# # Question 5 - Is Unique : Implement an algorithm to determine if a list has all unique characters, using python list.
# myList = [1, 20, 30, 44, 5, 56, 8, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]


# def isUnique(list):
#     a = []
#     for i in list:
#         if i in a:
#             print(i)
#             return False
#         else:
#             a.append(i)
#     return True


# print(isUnique(myList))


# # Question - 6 Permutation
# def permutation(list1, list2):
#     if len(list1) != len(list2):
#         return False
#     list1.sort()
#     list2.sort()
#     if list1 == list2:
#         return True
#     else:
#         return False


# list1 = ["a", "b", "c"]
# list2 = ["a", "c", "b"]
# print(permutation(list1, list2))


# Question 7 - Rotate a matrix by 90 degrees
import numpy as np

myArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def rotateMatrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            # Save top element
            top = matrix[layer][i]
            # move left element to top
            matrix[layer][i] = matrix[-i - 1][layer]
            # move bottom element to left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            # move right to bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]
            # move to the right
            matrix[i][-layer - 1] = top
    return matrix


print(rotateMatrix(myArray))
