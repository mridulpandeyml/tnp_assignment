def maxDifference(nums):
    n=len(nums)
    mx=[nums[n-1]]*n
    mi=[nums[0]]*n
    difference=-1
    for i in range(1,n):
        mi[i]=min(mi[i-1],nums[i])
        mx[n-1-i]=max(mx[n-i],nums[n-1-i])
    for i in range(n):
        difference=max(difference,mx[i]-mi[i])
    if difference==0:
        return -1
    else:
        return difference
    
nums=[1,6,3,8,8,5,3]
print(maxDifference(nums))