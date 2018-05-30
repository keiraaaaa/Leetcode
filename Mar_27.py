'''
##############
# 69. Sqrt(x)
##############
# Using binary search
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        left = 1
        right = x        
        while True:
            mid = int(left + (right-left)/2)
            if mid > x/mid:
                right = mid - 1
            elif mid+1 > x/(mid+1):
                return mid
            else:
                left = mid + 1
solu = Solution()
print (solu.mySqrt(8))
'''

##########################
# 88. Merge Sorted Array
##########################
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n >0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        nums1[:n] = nums2[:n]
        return nums1

solu = Solution()
nums1 = [0]
nums2 = [1]
m = 0
n = 1
print (solu.merge(nums1,0,nums2,1))










