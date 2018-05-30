############################
# 226. Invert Binary Tree
############################
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
        	root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        	return root

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
t.right.left = TreeNode(6)
t.right.right = TreeNode(7)
print (t.left.left.val)
print (t.left.val)
solu = Solution()
newt = solu.invertTree(t)
print (newt.right.right.val)
print (newt.right.val)
'''
'''
######## my version ########
############################
# 234. Palindrom Linked List
############################
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """    
        # while head:
        # 	if head.val != new.val:
        # 		return False
        # 	head = head.next
        # 	new = new.next
        # return True
        headnew = head
        print (headnew.next)
        if head:
            prev = None
            while head:
                cur = head
                head = head.next
                cur.next = prev
                prev = cur
        print (headnew.next)


# test 1
# a = ListNode(1)
# a.next = ListNode(1)
# a.next.next = ListNode(2)
# a.next.next.next = ListNode(1)

# test 2
a = ListNode(0)
a.next = ListNode(1)
# print (a.next.val)
solu = Solution()
print (solu.isPalindrome(a))
# b = solu.inv(a)
# print (b.val)
# print (a.val)

# prev = None
# head = a
# while head:
#     cur = head
#     head = head.next
#     cur.next = prev
#     prev = cur
# print(cur.next.next.val)
'''

##### solution version #####
############################
# 234. Palindrom Linked List
############################
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, slow, rev.next = slow, slow.next, rev
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        return not rev
# test 1
a = ListNode(1)
a.next = ListNode(1)
a.next.next = ListNode(2)
a.next.next.next = ListNode(1)
solu = Solution()
print (solu.isPalindrome(a))




