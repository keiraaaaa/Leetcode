'''
##############################
# 21. Merge Two Sorted Lists
##############################
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sol = cur = ListNode(0)
        while l1 and l2:
        	if l1.val <= l2.val:
        		cur.next = l1
        		l1 = l1.next
        	else:
        		cur.next = l2
        		l2 = l2.next
        	cur = cur.next
        cur.next = l1 or l2
        return sol.next

'''
##############################
# 53. Maximum Subarray
##############################
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return False

        curmax = arrmax = nums[0]
        for i in nums[1:]:
        	curmax = max(i, curmax+i)
        	arrmax = max(curmax, arrmax)
        return arrmax


# a = ListNode(0)
# b = ListNode(1)
# a.next = b
# node = a.head
# while node:
#     print (node.value)
#     node = node.next
# print (a.next.val)
# c = ListNode(3)
# c.next = a
# print (c.next.next.val)
