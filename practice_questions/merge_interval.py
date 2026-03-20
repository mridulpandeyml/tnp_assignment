# 56. Merge Intervals
#https://leetcode.com/problems/merge-intervals/submissions/1954240992

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        merged=[intervals[0]]
        for i in intervals[1:]:
            if i[0]<=merged[-1][1]:
                merged[-1]=[merged[-1][0],max(merged[-1][1],i[1])]
            else:
                merged.append(i)
        return merged 
        