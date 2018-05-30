############
# 15. 3Sum
############
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums = sorted(nums)
        t = []
        for i in range (len(nums)-2):
            if i==0 or (i>0 and nums[i]>nums[i-1]):
                target = 0 - nums[i]
                l, r = i+1, len(nums)-1
                while l<r:
                    if nums[l]+nums[r]==target:
                        t.append([nums[i],nums[l],nums[r]])
                        while l+1<r and nums[l]==nums[l+1]:
                            l += 1
                        while l<r-1 and nums[r]==nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[l]+nums[r]<target:
                        l += 1
                    else:
                        r -= 1

        return t



nums = [-1, 0, 1, 2, -1, -4]
solu = Solution()
print (solu.threeSum(nums))