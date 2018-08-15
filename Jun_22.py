'''
#####################################
# 494. Target Sum
#####################################
class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        cache = {}
        return self.bfs(0, S, nums, cache)

    def bfs(self, i, S, nums, cache):
        print(cache)
        if i==len(nums) and S==0:
            return 1
        if i==len(nums) and S!=0:
            return 0
        if (i, S) in cache:
            return cache[(i,S)]
        count = self.bfs(i+1, S+nums[i], nums, cache)+self.bfs(i+1, S-nums[i], nums, cache)
        cache[(i, S)] = count
        return cache[(i, S)]

nums = [3]
S = 3
nums = [10,9,6,4,19,0,41,30,27,15,14,39,33,7,34,17,24,46,2,46]
S = 45
nums = [1,1,1,1,1]
S = 3
solu = Solution()
print (solu.findTargetSumWays(nums, S))
'''
'''
#####################################
# 560. Subarray Sum Equals K
#####################################
class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {0:1}
        res, total = 0, 0
        for num in nums:
            total += num
            res += dic.get(total-k, 0)
            dic[total] = dic.get(total, 0) + 1
        return res

nums = [1,1,1]
k = 2
nums = [1,2,5,5,4,2]
k = 5
solu = Solution()
print (solu.subarraySum(nums, k))
'''
'''
#####################################
# 621. Task Scheduler
#####################################
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if not tasks: return 0
        f = {}
        for task in tasks:
            f[task] = f.get(task, 0) + 1
        frq = sorted(f.values(), reverse=True)
        i = 0
        count = 0
        while i<len(frq) and frq[i]==frq[0]:
            count += 1
            i += 1
        if i>=len(frq):
            if n>=count: return frq[0]*count+(n+1-count)*(frq[0]-1)
            else: return frq[0]*count
        else:
            s = sum(frq[i:])
            if n>=count: return frq[0]*count+max((n+1-count)*(frq[0]-1), s)
            else: return frq[0]*count+s           

# tasks = ["A","A","A","B","B","B"]
# n = 2
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
solu = Solution()
print (solu.leastInterval(tasks, n))
'''
'''
#####################################
# 647. Palindromic Substrings
#####################################
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count, l = len(s),len(s)
        for i in range(l):
            j, k = i-1, i+1
            while j>=0 and k<=l:
                if self.check(s[j:k])==True: count+=1
                else: break
                j -= 1
                k += 1
        for i in range(l):
            j, k = i-1, i+2
            while j>=0 and k<=l:
                if self.check(s[j:k])==True: count+=1
                else: break
                j -= 1
                k += 1
        return count

    def check(self, s):
        if s==s[::-1]:
            return True
        else:
            return False

s = "aaa"
solu = Solution()
print (solu.countSubstrings(s))
'''
'''
#####################################
# 237. Delete Node in a Linked List
#####################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
'''
'''
#####################################
# 242. Valid Anagram
#####################################
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if sorted(s)==sorted(t):
            return True
        return False

s = "anagram"
t = "nagaram"
'''

#####################################
# 268. Missing Number
#####################################
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        l = len(nums)
        return int(l*(l+1)/2-s)

nums = [3,0,1]
solu = Solution()
print (solu.missingNumber(nums))













