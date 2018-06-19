'''
##################################################################
# 105. Construct Binary Tree from Preorder and Inorder Traversal
##################################################################
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(instart, inend, prestart, preorder, inorder):
            if prestart>len(preorder)-1 or inend<instart:
                return None
            root = TreeNode(preorder[prestart])
            inindex = inorder.index(root.val)
            root.left = helper(instart, inindex-1, prestart+1, preorder, inorder)
            root.right = helper(inindex+1, inend, prestart+inindex-instart+1, preorder, inorder)
            return root

        if preorder and inorder is None:
            return None
        return helper(0, len(inorder)-1, 0, preorder, inorder)


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
solu = Solution()
r = solu.buildTree(preorder, inorder)
print (r.right.right.val)
'''

###########################################
# 114. Flatten Binary Tree to Linked List
###########################################
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        r = root
        while r:
            if r.left:
                pre = r.left
                while pre.right:
                    pre = pre.right
                pre.right = r.right
                r.right = r.left
                r.left = None
            r = r.right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)
solu = Solution()
solu.flatten(root)







