##################################
# 98. Validate Binary Search Tree
##################################
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root):
        if not root: return True

        res = self.inorder(root.left)
        if self.prev>=root.val:
            return False
        else:
            self.prev=root.val

        return res and self.inorder(root.right)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = -float('inf')
        return self.inorder(root)



root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)
solu = Solution()
print (solu.isValidBST(root))





