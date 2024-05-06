# Dictionary Methods

# myDict = {"name": "Edy", "age": 26, "address": "London", "education": "master"}

# myDict.clear()
# print(myDict)


# # Copy Method
# newDict = myDict.copy()
# print(newDict)
# print(myDict)


# # fromkeyys() method
# newDict = {}.fromkeys([1, 2, 3], 0)
# print(newDict)


# # get() method
# print(myDict.get("age", 27))  # if the key exists in Dict --> it will return key value
# print(
#     myDict.get("city", 27)
# )  # if the key does not exist in Dict --> It will return specified default value which is 27


# # items() method --> return key value Tuple paris
# print(myDict.items())


# # keys() method --> Returns all keys in the Dict
# print(myDict.keys())


# # popitem() method --> removes an arbitary element from the Dict
# print(myDict.popitem())
# print(myDict)


# # detdefault() --> returns key value in the dict, if not returns specified default value, or return none if default value is not specified
# print(myDict.setdefault("name", "added"))
# print(myDict)


# # pop() method --> removes last element form the dict, if key is specified -> key with value is removed
# print(myDict.pop("name", "not"))


# # values() method --> return all the values in the Dict
# print(myDict.values())


# # update() method --> adds elements to the dict, if the key is not in the Dict
# newDict = {"a": 1, "b": 2, "c": 3}
# myDict.update(newDict)
# print(myDict)


# operations and built in functions

# myDict = {"one": "uno", "two": "dos", "three": "tres", "four": "cuarto"}
# print(
#     "uno" in myDict.values()
# )  # for checking values in Dict --> very efficient Time Complx - O(1)


# for key in myDict:   # for getting all keys and values in a Dict
#     print(key, myDict[key])


# all() method - return True when all elements in iterables are true, else returns False
# myDict = {0: False, 1: False}
# print(all(myDict))


# # len() method - return len of the dict
# myDict = {0: False, 1: False}
# print(len(myDict))


# # sorted() method
# myDict = {"e": 1, "a": 2, "u": 3, "o": 4, "i": 5}
# print(sorted(myDict, reverse=False))

myDict = {"ae": 1, "aaa": 2, "uyr": 3, "ods": 4, "idafa": 5}
print(sorted(myDict, key=len))
