def productself(nums):
    n=len(nums)
    left=[1]*n
    right=[1]*n
    for i in range(1,n):
        left[i]=left[i-1]*nums[i-1]
        right[n-i-1]=right[n-i]*nums[n-i]
    ans=[0]*n
    for i in range(0,n):
        ans[i]=left[i]*right[i]
    return ans 

nums=[1,8,3,7]
print(productself(nums))   
