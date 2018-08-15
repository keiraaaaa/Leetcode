'''
#####################################
# 238. Product of Array Except Self
#####################################
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums:
            res = [0] * len(nums)
            res[0] = 1
            for i in range (1, len(nums)):
                res[i] = res[i-1] * nums[i-1]
            right = 1
            for j in range (len(nums)-1, -1, -1):
                res[j] *= right
                right *= nums[j]
            return res

nums = [1]
solu = Solution()
print (solu.productExceptSelf(nums))
'''
'''
#####################################
# 240. Search a 2D Matrix II
#####################################
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return self.dfs(matrix, 0, 0, target)

    def dfs(self, matrix, i, j, target):
        if i>=len(matrix) or j>=len(matrix[0]) or matrix[i][j]=='*' or matrix[i][j]>target:
            return False
        if matrix[i][j]==target:
            return True
        matrix[i][j] = '*'
        return self.dfs(matrix, i+1, j, target) or self.dfs(matrix, i, j+1, target)


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20
matrix = [[]]
target = 1
solu = Solution()
print (solu.searchMatrix(matrix, target))
'''
'''
#####################################
# 279. Perfect Squares
#####################################
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return n
        sq = []
        i = 1
        while i**2<=n:
            sq.append(i**2)
            i += 1
        stack = [n]
        count = 0
        while stack:
            count += 1
            temp = []
            for num in stack:
                for x in sq:
                    if num==x:
                        return count
                    if num<x:
                        break
                    temp.append(num-x)
            stack = temp

n = 13
solu = Solution()
print (solu.numSquares(n))
'''

#####################################
# 287. Find the Duplicate Number
#####################################
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            slow, fast = nums[0], nums[nums[0]]
            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]
            fast = 0
            while fast != slow:
                fast = nums[fast]
                slow = nums[slow]
            return slow



nums = [1,3,4,2,2]
solu = Solution()
print (solu.findDuplicate(nums))









