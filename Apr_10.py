'''
############################
# 39. Combination Sum
############################
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [],res)
        return res

    def dfs(self, candidates, target, i, temp, res):
        if target==0:
            return res.append(temp)
        for i in range (i, len(candidates)):
            if candidates[i] > target:
                break
            self.dfs(candidates, target-candidates[i], i, temp+[candidates[i]], res)



solu = Solution()
target = 7
candidates = [2, 3, 6, 7]
print (solu.combinationSum(candidates, target))
'''

############################
# 46. Permutations
############################
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.find([], res, nums)
        return res 

    def find(self, temp, res, nums):
        if not nums:
            return res.append(temp)
        for i in range (len(nums)):
            self.find(temp+[nums[i]], res, nums[:i]+nums[i+1:])

nums = [1,2,3]
solu = Solution()
print (solu.permute(nums))










