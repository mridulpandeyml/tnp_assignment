def subarraySum(nums):
    prefix=0
    maximum=float('-inf')
    for i in range(len(nums)):
        prefix+=nums[i]
        maximum=max(maximum,prefix)
        if(prefix<0):
            prefix=0
    return maximum

arr=[-2,1,-3,4,-1,2,1,-5,4]
print(subarraySum(arr))