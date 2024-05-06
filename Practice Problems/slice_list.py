# mylist = ["a", "b", "c", "d", "e", "f"]
# mylist[0:2] = ["x", "y"]
# print(mylist[:])

# # pop method
# mylist.pop(1)  # Here 1 is index
# print(mylist)

# mylist.pop()  # Here pop method deletes last element, if index is not specified
# print(mylist)

# # Delete method
# del mylist[2:4]
# print(mylist)

# # Remove method
# mylist.remove("e")
# print(mylist)

# # Searching for an element in the list
# myList = [10, 20, 30, 40, 50, 60, 70, 80]

# if 20 in myList:
#     print(myList.index(20))
# else:
#     print("The value does not exist in the list")


# def searchinlist(list, value):
#     for i in list:
#         if i == value:
#             return list.index(value)
#     return "The value does not exist in the list"


# print(searchinlist(myList, 10))


# List Operations / Functions
# (+) operator
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)

# # (*) Operator
# a = [0]
# a = a * 4
# print(a)

# a = [0, 1, 2, 3, 4, 5, 6]
# print(len(a))  # returns the no.of elements in the list

# print(max(a))  # returns max. element in the list

# print(min(a))  # returns min. element in the list

# print(sum(a))  # return sum of the elements in the list

# print(sum(a) / len(a))  # average of the elements in the list

newList = list()
while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    value = float(inp)
    newList.append(value)
average = sum(newList) / len(newList)

print("Average", average)
