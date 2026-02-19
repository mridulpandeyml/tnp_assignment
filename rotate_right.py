
def rotate( nums, k):
    start=0
    k=k%len(nums)
    end=len(nums)-1
    endm=end-k
    startm=endm+1
    while(start<=endm):
        nums[start],nums[endm]=nums[endm],nums[start]
        start=start+1
        endm=endm-1

    while(startm<=end):
        nums[startm],nums[end]=nums[end],nums[startm]
        startm=startm+1
        end=end-1
    start=0
    end=len(nums)-1
    while(start<=end):
        nums[start],nums[end]=nums[end],nums[start]
        start=start+1
        end=end-1

arr=[1,3,6,4,7]
k=3
rotate(arr,k)
print(arr)
    
    