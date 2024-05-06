import math
def binarySearch(array,value):
    start = 0
    end = len(array)-1
    mid = math.floor((start + end)/2)
    while not(array[mid] ==value) and end >= start:
        if value < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
        mid = math.floor((start+end)/2)
    if array[mid] == value:
        return mid
    else:
        return -1

cusArray = [8,9,12,15,17,19,20,21,28]
print(binarySearch(cusArray,10))