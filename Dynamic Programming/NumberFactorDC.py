#Top Down Approach
#Expressing a number as the sum of specific numbers: 
#This is a problem often encountered in computer science and 
#mathematics, where the goal is to express a number as the 
#sum of specific numbers3. For example, the number 5 can 
#be expressed as the sum of 1, 3, and 4 in six different ways3.

def numberFactorTD(n, tempDict):
    if n in (0,1,2):
        return 1
    elif n == 3:
        return 2
    else:
        if n not in tempDict:
            subP1 = numberFactorTD(n-1, tempDict)
            subP2 = numberFactorTD(n-3, tempDict)
            subP3 = numberFactorTD(n-4, tempDict)
            tempDict[n] = subP1 + subP2 + subP3
        return tempDict[n]
# print(numberFactorTD(5, {}))


# Bottom up Approach
def numberFactorBU(n):
    tempArr = [1,1,1,2]
    for i in range(4,n+1):
        tempArr.append(tempArr[i-1] + tempArr[i-3]+ tempArr[i-4])
    return tempArr[n]

print(numberFactorBU(5))