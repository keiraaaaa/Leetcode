'''
###################################
# 538. Convert BST to Greater Tree
###################################
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.val = 0
        def visit(root):
            if root:
                visit(root.right)
                root.val += self.val
                self.val = root.val
                visit(root.left)
                return root
        visit(root)
        return root

t = TreeNode(5)
t.left = TreeNode(3)
t.right = TreeNode(7)
t.left.left = TreeNode(2)
t.left.right = TreeNode(4)
t.right.left = TreeNode(6)
t.right.right = TreeNode(8)
solu = Solution()
q = solu.convertBST(t)
print (q.val)

'''
'''
###################################
# 543. Diameter of Binary Tree
###################################
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.val = 0
        def height(root):
            if root:
                l = height(root.left)
                r = height(root.right)
                self.val = max(self.val,l+r)
                return max(l,r)+1
            else:
                return 0
        height(root)
        return self.val

t = TreeNode(5)
t.left = TreeNode(3)
t.right = TreeNode(7)
t.left.left = TreeNode(2)
t.left.right = TreeNode(4)
# t.right.left = TreeNode(6)
# t.right.right = TreeNode(8)
solu = Solution()
print (solu.diameterOfBinaryTree(t))
'''
'''
###############################
# 572. Subtree of Another Tree
###############################
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        if self.isMatch(s,t):
            return True         
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

    def isMatch(self, s,t):
        if not(s or t):
            return True
        elif(s and t):
            if s.val == t.val:
                return self.isMatch(s.left, t.left) and self.isMatch(s.right, t.right)
        else:
            return False


t = TreeNode(5)
t.left = TreeNode(3)
t.right = TreeNode(7)
# t.left.left = TreeNode(2)
t.left.right = TreeNode(4)
q = TreeNode(3)
q.left = TreeNode(2)
q.right = TreeNode(4)
solu = Solution()
print (solu.isSubtree(t,q))
'''
'''
###############################
# 617. Merge Two Binary Trees
###############################
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
        else:
            return t1 or t2
        return root
'''
'''
##############################################
# 581. Shortest Unsorted Continuous Subarray
##############################################
class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        is_same = [a==b for a, b in zip(nums, sorted(nums))]
        if all(is_same):
            return 0
        else:
            return len(nums)-is_same[::-1].index(False)-is_same.index(False)

a = [2, 6, 4, 8, 10, 9, 15]
print (a.index(4))
'''

#####################
# 7. Reverse Integer
#####################
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        b = str(x)
        if b[0] == '-':
            if b[-1] == 0:
                s = -int(b[1:-1][::-1])
            else:
                s = -int(b[1:][::-1])
        else:
            if b[-1] == 0:
                s = int(b[:-1][::-1])
            else:
                s = int(b[::-1])
        if abs(s) > 2**31:
            return 0 
        else:
            return s                       













