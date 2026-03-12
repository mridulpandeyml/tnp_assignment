def removeDuplicates(nums):
    start=0
    for i in range(1,len(nums)):
        if nums[start]!=nums[i]:
            start+=1
            nums[start]=nums[i]
    return nums[:start+1]

nums=[1,2,2]
print(removeDuplicates(nums))
