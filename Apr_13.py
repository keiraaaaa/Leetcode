'''
################
# 55. Jump Game
################
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or (nums[0]==0 and len(nums)>1):
            return False
        if len(nums)==1:
            return True
        l = len(nums)
        max_ = 0
        for i in range (l-1):
            if nums[i]+i>max_:
                max_ = nums[i] + i
            if max_>=l-1:
                return True
            if max_==i and nums[i]==0:
                return False
        return False

# nums = [2,3,1,1,4]
nums = [1,2,0,3,0]
solu = Solution()
print (solu.canJump(nums))
'''

########################
# 56. Merge Intervals
########################
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals
        out = []
        for interval in sorted(intervals, key=lambda i: i.start):
            if out and interval.start<=out[-1].end:
                out[-1].end = max(interval.end, out[-1].end)
            else:
                out.append(interval)
        return out
intervals = [Interval(2,3), Interval(8,10),Interval(1,6),Interval(15,18)]
# intervals = [[2,3],[8,10],[1,6],[15,18]]
solu = Solution()
t = solu.merge(intervals)
print (t[1].end)
# print (sorted(intervals, key=lambda i: i.start))











