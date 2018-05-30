##########################
# 141. Linked List Cycle
##########################
# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         try:
#         	slow = head
#         	fast = head.next
#         	while slow is not fast:
#         		slow = slow.next
#         		fast = fast.next.next
#         	return True
#         except:
#         	return False
# t = ListNode(3)
# print (t.val)



###################
# 155. Min Stack
###################

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf') 
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.stack == []:
        	self.min = float('inf')
        if x < self.min:
        	self.min = x
        self.stack.append((x, self.min))
        
        

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        if self.stack:
        	self.min = self.stack[-1][1]
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]

        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-10)
obj.push(14)
obj.push(-20)
obj.pop()
obj.push(10)
print (obj.stack)
obj.push(-7)
param_3 = obj.top()
param_4 = obj.getMin()

print (obj.stack)
print (param_3)
print (param_4)

# a = []
# print (a == [])
# "push" -10
# "push" 14
# push(-20)
# pop()
# push(10)
# push(-7)

# Input:
# ["MinStack","push","push","getMin","getMin","push","getMin","getMin","top","getMin","pop","push","push","getMin","push","pop","top","getMin","pop"]
# [[],[-10],[14],[],[],[-20],[],[],[],[],[],[10],[-7],[],[-7],[],[],[],[]]
# Output:
# [null,null,null,-10,-10,null,-20,-20,-20,-20,null,null,null,-20,null,null,-7,-20,null]
# Expected:
# [null,null,null,-10,-10,null,-20,-20,-20,-20,null,null,null,-10,null,null,-7,-10,null]
