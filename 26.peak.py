def PeakElement(nums):
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            return nums[i]
    return nums[len(nums)-1]

nums=[1,2,3,2]
print(PeakElement(nums))