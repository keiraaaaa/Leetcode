#########################
# 198. House Robber
#########################
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0
        elif len(nums) == 1:
        	return nums[0]
        else:
	        dp = [nums[0], max(nums[0], nums[1])]
	        for i in nums[2:]:
	        	dp.append(max(dp[-2] + i, dp[-1]))
	        return dp[-1]
# nums = [2]
# s = Solution()
# print (s.rob(nums))


############################
# 206. Reverse Linked List
############################
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
        	prev = None
        	while head:
        		cur = head
        		head = head.next
        		cur.next = prev
        		prev = cur
        	return cur

t = ListNode(1)
t.next = ListNode(2)
t.next.next = ListNode(3)
s = Solution()
p = s.reverseList(t)
print (p.val, p.next.val)



