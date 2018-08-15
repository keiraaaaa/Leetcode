'''
#####################################
# 300. Longest Increasing Subsequence
#####################################
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tail = [0] * len(nums)
        size = 0
        for num in nums:
            i, j = 0, size
            print (i, j)
            while i!=j:
                m = (i+j)//2
                if tail[m]<num:
                    i = m + 1
                else:
                    j = m
            tail[j] = num
            size = max(j+1, size)
            print (tail)
        return size

nums = [10,9,2,5,3,7,101,18]
solu = Solution()
print (solu.lengthOfLIS(nums))
'''
'''
#####################################
# 322. Coin Change
#####################################
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0:
            return 0
        stack = [amount]
        visited = [False] * amount
        count = 0
        visited[-1] = True
        while stack:
            count += 1
            temp = []
            for money in stack:
                for i in coins:
                    t = money-i
                    if t==0: return count
                    if t>0 and visited[t-1]==False:
                        temp.append(money-i)
                        visited[t-1] = True
                stack = temp
        return -1

coins = [357,239,73,52]
amount = 9832
coins = []
amount = 1
solu = Solution()
print (solu.coinChange(coins, amount))
'''
'''
#####################################
# 337. House Robber III
#####################################
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.maxmoney(root)
        return max(res[0], res[1])
    
    def maxmoney(self, root):
        if root==None: return [0, 0]
        left = self.maxmoney(root.left)
        right = self.maxmoney(root.right)
        res = [0, 0]
        res[0] = max(left[0],left[1]) + max(right[0], right[1])
        res[1] = root.val + left[0] + right[0]
        return res

root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(3)
root.right.right = TreeNode(1)
solu = Solution()
print (solu.rob(root))
'''
'''
#####################################
# 338. Counting Bits
#####################################
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        l = [0,1,1,2]
        if num<4: return l[:num+1]
        while len(l)<=num:
            temp = l + [x+1 for x in l]
            l = temp
        return l[:num+1]

num = 10
solu = Solution()
print (solu.countBits(num))
'''

#####################################
# 347. Top K Frequent Elements
#####################################
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        f = {}
        for i in range (len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        for i in count:
            if count[i] not in f:
                f[count[i]] = [i]
            else:
                f[count[i]].append(i)
        l = []
        t = sorted(f, reverse=True)
        i = 0
        while k>0:
            l += f[t[i]]
            k -= len(f[t[i]])
            i += 1
        return l

nums = [1,2]
k = 2
solu = Solution()
print (solu.topKFrequent(nums, k))












