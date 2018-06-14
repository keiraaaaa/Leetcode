########################################
# 102. Binary Tree Level Order Traversal
########################################
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root: return []
        s = []
        temp = [root]
        while temp:
            s.append([i.val for i in temp])
            temp_next = []
            for i in temp:
                if i.left: temp_next.append(i.left)
                if i.right: temp_next.append(i.right)
            temp = temp_next
        return s



root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)
solu = Solution()
print (solu.levelOrder(root))
# a = []
# a.append(root)
# a.append(root.left)
# print (a[0].val)



