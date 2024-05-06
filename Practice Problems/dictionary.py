# update / add an element to the dictionary

# myDict = {"name": "Edy", "age": 26}
# myDict["age"] = 27  # updating an element in Dict
# print(myDict)

# # adding an element

# myDict["address"] = "London"
# print(myDict)

# Traverse through a dictionary
myDict = {"name": "Edy", "age": 26, "address": "London"}

# def traverseDict(dict):
#     for key in dict:
#         print(key, dict[key])


# traverseDict(myDict)


##Traversing through a dictionary

# def searchDict(dict, value):
#     for key in dict:
#         if dict[key] == value:
#             return key, value
#     return "The value does not exist"


# print(searchDict(myDict, 26))

# # Delete an element from a dictionary

# print(myDict.pop("name"))
# print(myDict)

# print(myDict.popitem())
# print(myDict)


# Delete any element from the Dict

# myDict.clear()
# print(myDict)

# del myDict["age"] # used to delete key with value
# print(myDict)

# del myDict  # used to delete entire dict
# print(myDict)
