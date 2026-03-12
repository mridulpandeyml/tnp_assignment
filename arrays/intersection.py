
def intersection(nums1, nums2):
    
    ans=[]
    count={}
    for num in nums1:
        
        count[num]=1
    
    for num in nums2:
        if num in count and count[num]>0:
            ans.append(num)
            count[num]=0
    return ans


nums1=[1,2,3,4,5,6,7]
nums2=[4,5,6,7,8,9]
print(intersection(nums1,nums2))

