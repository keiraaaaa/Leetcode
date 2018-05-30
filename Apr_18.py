'''
##############
# 78. Subsets
##############
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        res = [[nums[0]]]
        for i in range(1,len(nums)):
            res = self.find(res,nums[i])+[[nums[i]]]
        return res+[[]]
    def find(self,res,num):
        temp = res + [i+[num] for i in res]
        return temp

nums = []
solu = Solution()
print (solu.subsets(nums))
'''
'''
##################
# 79. Word Search
##################
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range (len(board[0])):
                if self.check(i,j,board,word):
                    return True
        return False

    def check(self, i, j, board, word):
        if not word: return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        t = board[i][j]
        board[i][j] = '0'
        res = self.check(i+1,j,board,word[1:]) or self.check(i-1,j,board,word[1:]) \
        or self.check(i,j+1,board,word[1:]) or self.check(i,j-1,board,word[1:])
        board[i][j] = t
        return res

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCB"
solu = Solution()
print (solu.exist(board, word))
'''
'''
####################################
# 94. Binary Tree Inorder Traversal
####################################
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return []
        return self.inorder(res, root)

    def inorder(self, res, root):
        if root:    
            self.inorder(res, root.left)
            res.append(root.val)
            self.inorder(res, root.right)
        return res
root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)
solu = Solution()
print (solu.inorderTraversal(root))
'''

####################################
# 96. Unique Binary Search Trees
####################################
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0: return 0
        if n==1: return 1
        s = [0 for i in range(n+1)]
        s[0], s[1] = 1, 1
        for i in range(2,n+1):
            total = 0
            for j in range (0,i):
                total += s[j] * s[i-1-j]
            s[i] = total    
        return total

solu = Solution()
n = 0
print (solu.numTrees(n))





















