'''
#####################################
# 33. Search in Rotated Sorted Array
#####################################
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        i = 0
        while i<len(nums):
            if nums[i]==target:
                return i
            i += 1
        return -1
'''

#####################################
# 34. Search for a Range
#####################################
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        def search(start,end):
            if nums[start]==target==nums[end]:
                return [start, end]
            if nums[start] <= target <= nums[end]:
                mid = start + (end-start)//2
                l, r = search(start, mid), search(mid+1, end)
                return max(l,r) if -1 in l+r else [l[0],r[1]]
            return [-1, -1]
        return search(0, len(nums)-1)


nums = [8]
target = 8
solu = Solution()
print (solu.searchRange(nums, target))















