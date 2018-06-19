'''
################################
# 152. Maximum Product Subarray
################################
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return False
        if len(nums)==1: return nums[0]
        p, n = [0] * len(nums), [0] * len(nums)
        if nums[0]>0:
            p[0] = nums[0]
        if nums[0]<0:
            n[0] = nums[0]
        for i in range (1,len(nums)):
            if nums[i]>0:
                if p[i-1]>0: p[i] = p[i-1]*nums[i]
                if p[i-1]==0: p[i] = nums[i]
                if n[i-1]<0: n[i] = n[i-1] * nums[i]
            if nums[i]<0:
                if n[i-1]<0: 
                    p[i] = n[i-1] * nums[i]
                    n[i] = nums[i]
                if n[i-1]==0: n[i] = nums[i]                
                if p[i-1]>0: n[i] = p[i-1] * nums[i]
        print (p,n)
        return max(p)

nums = [2,-5,-2,-4,3]
# nums = [-2, 0, -1]
solu = Solution()
print (solu.maxProduct(nums))
'''

#########################
# 200. Number of Islands
#########################
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            count = 0
            return count
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!='1':
            return
        grid[i][j] = '*'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
solu = Solution()
print (solu.numIslands(grid))

















