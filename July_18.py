'''
################################################
# 103. Binary Tree Zigzag Level Order Traversal
################################################
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        stack = [root]
        out = [[root.val]]
        j = 1
        while stack:
            stack_temp, temp = [], []
            if j==1:
                for i in stack[::-1]:
                    if i.right:
                        temp.append(i.right.val)
                        stack_temp.append(i.right)
                    if i.left:
                        temp.append(i.left.val)
                        stack_temp.append(i.left)
            if j==0:
                for i in stack[::-1]:
                    if i.left:
                        temp.append(i.left.val)
                        stack_temp.append(i.left)
                    if i.right:
                        temp.append(i.right.val)
                        stack_temp.append(i.right)
            j = 1-j
            if temp:
                out.append(temp)
            stack = stack_temp
        return out

x = TreeNode(3)
x.left = TreeNode(9)
x.right = TreeNode(20)
x.right.left = TreeNode(15)
x.right.right = TreeNode(7)
x.left.left = TreeNode(1)
x.left.right = TreeNode(2)
s = Solution()
print (s.zigzagLevelOrder(x))
'''

################################################＃#
# 116. Populating Next Right Pointers in Each Node
################################################＃#
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root:
            root.next = None
            pre, cur = root, root
            while pre:
                cur = pre
                while cur and cur.left:
                    cur.left.next = cur.right
                    # print (cur.val, cur.left.next.val)
                    if not cur.next:
                        cur.right.next = None    
                        # print (cur.right.val)
                    else:
                        cur.right.next = cur.next.left
                    cur = cur.next
                pre = pre.left          
        return root

x = TreeLinkNode(3)
x.left = TreeLinkNode(9)
x.right = TreeLinkNode(20)
# x.right.left = TreeNode(15)
# x.right.right = TreeNode(7)
# x.left.left = TreeNode(1)
# x.left.right = TreeNode(2)
s = Solution()
r = s.connect(x)
print (r.left.next.val)
# y = None
# if not y: print ('h')






