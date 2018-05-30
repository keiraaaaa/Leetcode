'''
##################################################
# 108. Convert Sorted Array to Binary Search Tree
##################################################
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        mid = int((len(nums)+int(len(nums)%2==1))/2-1)
        root = TreeNode(nums[mid])
        
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[(mid+1):])
        return root
nums = [-10,-3,0,5,9]
solu = Solution()
t = solu.sortedArrayToBST(nums)
print (t.val)
print (t.left.val)
print (t.left.right.val)
print (t.right.val)
print (t.right.right.val)
'''
'''
#########################
# 118. Pascal's Triangle
#########################
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]

        l, last = [[1],[1,1]],[1,1]
        j = 3
        while j <= numRows:
            temp = [1] + [last[i]+last[i+1] for i in range (len(last)-1)] + [1]
            l.append(temp)
            last = temp
            j += 1
        return l

numRows = 1
solu = Solution()
print (solu.generate(numRows))
'''
'''
###########################################
# 122. Best Time to Buy and Sell Stock II
###########################################
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        i = 1
        while i < len(prices):
            if prices[i] <= prices[i-1]:
                i += 1
            else:
                total -= prices[i-1]
                while i<len(prices) and prices[i]> prices[i-1]:
                    i += 1
                total += prices[i-1]
        return total

prices = [2,1,2,0,1]
solu = Solution()
print (solu.maxProfit(prices))
'''
'''
#####################################################
# 309. Best Time to Buy and Sell Stock with Cooldown
#####################################################
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)>1:
            buy,sell,prev_sell = -prices[0],0,0
            for price in prices:
                prev_buy = buy
                buy = max(prev_sell-price, prev_buy)
                prev_sell = sell
                sell = max(prev_buy+price, prev_sell)
            return sell
        else:
            return 0

prices = [1, 2, 3, 0, 2]
solu = Solution()
print (solu.maxProfit(prices))
'''

############################################################
# 714. Best Time to Buy and Sell Stock with Transaction Fee
############################################################
class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        prev_buy, prev_sell = -prices[0], 0
        for price in prices:
            buy = max(prev_buy, prev_sell-price)
            sell = max(prev_sell, prev_buy+price-fee)
            prev_buy,prev_sell = buy, sell
        return max(buy, sell)


prices = [1, 3, 2, 8, 4, 9]
fee = 2
solu = Solution()
print (solu.maxProfit(prices, fee))

















