########################################
# 160. Intersection of Two Linked Lists
########################################
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA and headB:
        	A, B = headA, headB
        	while A != B:
        		A = A.next if A.next else headB
        		B = B.next if B.next else headA
        	return A

# headA = ListNode(3)
# b = ListNode(4)
# headA.next = b
# headB = ListNode(5)
# # print (headA)
# # print (headA.next.val)
# A, B = headA.next, headB.next
# if A.next:
# 	A = A.next
# else:
# 	A = headB
# print (A.val)
# print (A)
# print (headB)