#########################
# 162. Find Peak Element
#########################
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            peak = 0
            return peak
        else:
            if nums[0]>nums[1]:
                peak = 0
                return peak
            if nums[-1]>nums[-2]:
                peak = len(nums)-1
                return peak
            for i in range (1,len(nums)-1):
                if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                    peak = i
                    return peak

s = Solution()
print(s.findPeakElement([1,2,1]))








