'''
#################################
# 5. Longest Palindromic Substring
#################################
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def palindrome(i):
            j = 0
            while i-j >= 0 and i+j < len(s) and s[i-j]==s[i+j]:
                j += 1
            left, maxlen = i-j+1, 2 * (j-1) +1
            j = 0
            while i-1-j >= 0 and i+j < len(s) and s[i-1-j]==s[i+j]:
                j += 1
            if maxlen < 2 * j:
                left, maxlen = i-j, 2 * j
            return left, maxlen

        if len(s)<2:
            return s
        maxlen = 0
        left = 0
        for i in range(1,len(s)):
            t_left, t_len = palindrome(i)
            print (i, t_left, t_len)
            if maxlen < t_len:
                maxlen, left = t_len, t_left
        if not maxlen:
            return s[0]  
        return s[left:left+maxlen]
s = "bb"
solu = Solution()
print (solu.longestPalindrome(s))
'''
'''
################################
# 11. Container With Most Water
################################
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_ = 0
        i, j = 0,len(height)-1
        while i < j:
            h = min(height[i], height[j])
            max_ = max(max_, h * (j-i))
            while j>i and height[j]<=h:
                j -= 1
            while j>i and height[i]<=h:
                i += 1
        return max_
height = [1,2,2,3,2,2,2,3]
solu = Solution()
print (solu.maxArea(height))
'''
'''
################################
# 202. Happy Number
################################
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        t = []
        i = n
        while i not in t:
            if i==1:
                return True
            t.append(i)
            str_i = str(i)
            q = 0
            for j in range(len(str_i)):
                q += int(str_i[j])**2
            i = q
        return False
n = 19
solu = Solution()
print (solu.isHappy(n))
'''
'''
####################
# 204. Count Primes
####################
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        l = [True for i in range(n)]
        l[0:2] = [False] * 2
        for i in range (2,n//2+1):
            if l[i]:
                l[i*i:n:i] = [False] * len(l[i*i:n:i])
        return sum(l)


        
        # # my shit
        # n = n-1        
        # if n<2:
        #     return 0
        # d = {x:1 for x in range(2,n+1)}
        # i = 2
        # while i<=n//2:
        #     if i in d:
        #         j = i
        #         while i*j <= n:
        #             if i*j in d:
        #                 del d[i*j]
        #             j += 1
        #     i += 1
        # return len(d)
        

n = 30
solu = Solution()
print (solu.countPrimes(n))
# a = [1,2,3,4,5]
# a[0:5:3] = [False,False]
# print (a)
'''
##########################
# 217. Contains Duplicate
##########################
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        return not len(set(nums))==len(nums)























