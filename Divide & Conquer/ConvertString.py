# Covert one String to Another with minimum operation in python

def findMinOperations(s1,s2,index1,index2):
    if index1 == len(s1):
        return len(s2)-index2
    if index2 == len(s2):
        return len(s1)-index1
    if s1[index1] == s2[index2]:
        return findMinOperations(s1,s2,index1+1,index2+1)
    else:
        deleteOp = 1 + findMinOperations(s1,s2,index1,index2+1)
        insertOp = 1 + findMinOperations(s1,s2,index1+1, index2)
        replaceOp = 1 + findMinOperations(s1,s2,index1+1, index2+1)
        return min(deleteOp, insertOp, replaceOp)
    
print(findMinOperations("table","tbrles",0,0))



