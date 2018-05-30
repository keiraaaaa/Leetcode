'''
######################
# 2. Add Two Numbers
######################
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_, l2_ = '', ''
        while l1:
            l1_ += str(l1.val)
            l1 = l1.next
        while l2:
            l2_ += str(l2.val)
            l2 = l2.next
        t = str(int(l1_[::-1]) + int(l2_[::-1]))[::-1]
        s = ListNode(t[0])
        q = s
        if len(t) > 1:
            for i in range (1,len(t)):
                s.next = ListNode(t[i])
                s = s.next
        return q

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
solu = Solution()
print(solu.addTwoNumbers(l1, l2))
'''
'''
####################################################
# 3. Longest Substring Without Repeating Characters
####################################################
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        maxlen = '' 
        temp = ''
        i = 0
        while i < len(s):
            while i < len(s) and s[i] not in temp:
                temp += s[i]
                i += 1
            if len(temp)>len(maxlen): 
                maxlen = temp
            if i < len(s):
                temp += s[i]
                temp = temp[temp.index(s[i])+1:]
                i += 1
        # print (temp,i,i<len(s),s[i] not in temp)
            print (i,temp)
        return len(maxlen)

a = "a"
solu = Solution()
print (solu.lengthOfLongestSubstring(a))
'''






