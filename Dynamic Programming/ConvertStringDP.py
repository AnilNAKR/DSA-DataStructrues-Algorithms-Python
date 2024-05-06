def findMinOperationBU(s1, s2, tempDict):
    for i1 in range(len(s1)+1):
        dictKey = str(i1)+'0'
        tempDict[dictKey] = i1
    for i2 in range(len(s2)+1):
        dictKey = '0'+str(i2)
        tempDict[dictKey] = i2
    
    for i1 in range(1,len(s1)+1):
        for i2 in range(1,len(s2)+1):
            if s1[i1-1] == s2[i2-1]:
                dictKey = str(i1)+str(i2)
                dictKey1 = str(i1-1)+str(i2-1)
                tempDict[dictKey] = tempDict[dictKey1]
            else:
                dictKey = str(i1)+str(i2)
                dictKeyD = str(i1-1)+str(i2)
                dictKeyI = str(i1)+str(i2-1)
                dictKeyR = str(i1-1)+str(i2-1)
                tempDict[dictKey] = 1 + min(tempDict[dictKeyD], min(tempDict[dictKeyI],tempDict[dictKeyR]))
    dictKey = str(len(s1))+str(len(s2))
    return tempDict[dictKey]

s1 = "catch"
s2 = "carch"
s3 = "table"
s4 = "tbres"
print(findMinOperationBU(s1,s2,{}))
print(findMinOperationBU(s3,s4,{}))