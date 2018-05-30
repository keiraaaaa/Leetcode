'''
#########################
# 64. Minimum Path Sum
#########################
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        for i in range(len(grid)):
            for j in range (len(grid[0])):
                if i==0 and j!=0:
                    grid[i][j] = grid[i][j-1]+grid[i][j]
                if j==0 and i!=0:
                    grid[i][j] = grid[i-1][j]+grid[i][j]
                if i!=0 and j!=0:
                    grid[i][j] = min(grid[i-1][j],grid[i][j-1])+grid[i][j]
        return grid[-1][-1]

grid = [[1,3,1], [1,5,1], [4,2,1]]
solu = Solution()
print (solu.minPathSum(grid))
'''

#########################
# 75. Sort Colors
#########################
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums:
            p0, p2 = 0, len(nums)-1
            i = 0
            while i<=p2:
                while i<p2 and nums[i]==2:
                    nums[i], nums[p2] = nums[p2], nums[i]
                    p2 -= 1
                while i>p0 and nums[i]==0:
                    nums[i], nums[p0] = nums[p0], nums[i]
                    p0 += 1
                i += 1
            return nums


nums = [2,0,1]
solu = Solution()
print (solu.sortColors(nums))





