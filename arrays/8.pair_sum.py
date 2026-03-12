def twoSum(nums, target):
    n=len(nums)
    ans=[]
    for i in range(0,n):
        for j in range(1,n):
            if(nums[i]+nums[j]==target and i!=j):
                ans.append(i)
                ans.append(j)
                return ans
    
        