'''
############################
# 142. Linked List Cycle II
############################
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        slow, fast = head, head
        while fast.next!=None and fast.next.next!=None:
            slow = slow.next
            fast = fast.next.next           
            if fast == slow:
                cycle = True
                break;
        if fast.next==None or fast.next.next==None:
            return None
        else:
            # return True
            slow_new = head
            while slow_new != slow:
                slow_new = slow_new.next
                slow = slow.next
            return slow
x = []
x = ListNode(1)
# x.next = ListNode(2)
# x.next.next = ListNode(3)
# x.next.next.next = x.next
solu = Solution()
# print (x.next.next.next.val)
print (solu.detectCycle(x))
'''

###################
# 148. Sort List
###################
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def merge(self, l1, l2):
        merged = ListNode(0)
        tail = merged
        while l1!=None and l2!=None:
            if l1.val>l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next
        if l1==None:
            tail.next = l2
        if l2==None:
            tail.next = l1
        return merged.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        slow, fast = head, head
        while slow.next != None and fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        prev = slow.next
        slow.next = None
        # print (head.val, prev.val)
        return self.merge(self.sortList(head), self.sortList(prev))


x = ListNode(4)
x.next = ListNode(2)
x.next.next = ListNode(1)
x.next.next.next = ListNode(3)
solu = Solution()
s = solu.sortList(x)
print (s.val)













