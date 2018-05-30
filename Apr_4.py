'''
############################################
# 17. Letter Combinations of a Phone Number
############################################
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dict_ = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        t = ['']
        for d in digits:
            temp = []
            for y in t:
                for x in dict_[d]:
                    temp.append(y+x)
            t = temp
            # print (t)
        return t
solu = Solution()
digits = '23'
print (solu.letterCombinations(digits))
'''
'''
############################################
# 19. Remove Nth Node From End of List
############################################
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head:
            slow, fast = head, head
            i = 0
            while i < n:
                fast = fast.next
                i += 1
            if not fast:
                return head.next
            while fast.next:
                slow = slow.next
                fast = fast.next
            slow.next = slow.next.next
            return head
a = ListNode(1)
b = a
for i in range(2,6):
    b.next = ListNode(i)
    b = b.next
solu = Solution()
c = solu.removeNthFromEnd(a,5)
print (c.val)
# print (c.next.next.next.val)
'''
'''
###########################
# 22. Generate Parentheses
###########################
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(t,left,right,out=[]):
            if left: 
                generate(t+'(',left-1,right)
            if right>left: 
                generate(t+')',left,right-1)
            if not right:
                out.append(t)
            return out
        return generate('',n,n)

n = 3
solu = Solution()
print (solu.generateParenthesis(n))
'''

###########################
# 31. Next Permutation
###########################
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i,j = len(nums)-1,len(nums)-1
        while i>0 and nums[i]<=nums[i-1]:
            i -= 1
        k = i
        while j>k:
            nums[j],nums[k] = nums[k],nums[j]
            k+=1
            j-=1
        if i>0:
            k = i
            while nums[k]<=nums[i-1]:
                k += 1
            nums[i-1], nums[k] = nums[k],nums[i-1]
        return nums
nums = [1,1,2]
solu = Solution()
print (solu.nextPermutation(nums))


 


























