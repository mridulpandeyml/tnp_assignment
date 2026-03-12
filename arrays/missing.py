def missing(nums):
    total=sum(nums)
    n=len(nums)
    ans=(n*(n+1))//2
    return ans-total

nums=[1,2,3,5,0]
print(missing(nums))