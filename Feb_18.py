##############################
# 101. Symmetric Tree
##############################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def isSymmetric(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         if root is None:
#         	return True
#         else:
#         	return self.isMirror(root.left, root.right)

#     def isMirror(self, left, right):
#     	if left is None and right is None:
#     		return True
#     	if left is None or right is None:
#     		return False
#     	if left.val == right.val:
#     		outPair = self.isMirror(left.left, right.right)
#     		inPair = self.isMirror(left.right, right.left)
#     		return outPair and inPair
#     	else:
#     		return False

# t = TreeNode(2)
# t.left = TreeNode(1)
# t.right = TreeNode(1)
# s = Solution()
# # print (t.left)
# print (s.isSymmetric(t))

####################################
# 104. Maximum Depth of Binary Tree
####################################
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if not root:
#         	return 0
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# t = TreeNode(2)
# t.left = TreeNode(1)
# t.right = TreeNode(1)
# p = TreeNode(0)
# s = Solution()
# print (s.maxDepth(t))

#######################################
# 121. Best time to Buy and Sell Stock
#######################################
# class Solution:
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if prices==[]:
#         	return 0
#         else:
# 	        maxprofit = 0
# 	        minprice = prices[0]
# 	        for p in prices:
# 	        	minprice = min(p, minprice)
# 	        	profit_cur = p - minprice
# 	        	maxprofit = max(profit_cur, maxprofit)
# 	        return maxprofit
# t = []
# s = Solution()
# print (s.maxProfit(t))

#######################################
# 136. Single Number
#######################################
# class Solution:
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         res = 0
#         for num in nums:
#         	res ^= num
#         	print (res)
#         return res
# t = [1,2,3]
# s = Solution()
# print (s.singleNumber(t))

hash_table = {3:1,4:2}
print (hash_table.pop(3))
print (hash_table)


