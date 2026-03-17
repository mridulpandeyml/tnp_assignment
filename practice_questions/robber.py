# leetcode 198. House Robber
#https://leetcode.com/problems/house-robber/submissions/1951484316
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        money=[0]*len(nums)
        money[0]=nums[0]
        money[1]=max(nums[0],nums[1])

        for i in range(2,len(nums)):
            money[i]=max(money[i-1],money[i-2]+nums[i])

        return money[-1]
        