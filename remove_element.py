def remove(nums,k):
    count=0
    for i in range(len(nums)):
        if nums[i]==k:
            count+=1
            nums[i]=1e6
    nums.sort()
    return nums[:len(nums)-count]

nums=[1,1,2,3,7,1,5,1,8]
k=1
print(remove(nums,k))