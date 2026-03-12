def merge(nums1, m, nums2, n):
    for i in range(n):
        nums1[i+m]=nums2[i]
    nums1.sort()
    
nums1=[1,3,5,0,0,0]
nums2=[2,4,6]
merge(nums1,3,nums2,3)
print(nums1)