def sort012( nums):
    count=[0]*3
    for num in nums:
        count[num]+=1
    for i in range(count[0]):
        nums[i]=0
    for i in range(count[0],count[0]+count[1]):
        nums[i]=1
    for i in range(count[0]+count[1],len(nums)):
        nums[i]=2

nums=[1,1,1,2,1,0,0,0,1,0,2,0]
sort012(nums)
print(nums)