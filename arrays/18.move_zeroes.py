def move(nums):
    start=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[i],nums[start]=nums[start],nums[i]
            start+=1

nums=[1,0,4,0,0,3]
move(nums)
print(nums)
        