def RD(nums):
    output = [None]
    for i in range(len(nums)):
        if nums[i] != output[-1]:
            output.append(nums[i])
    
    return len(output) - 1
nums = [0,0,1,1,1,2,2,3,3,4]
print(RD(nums))