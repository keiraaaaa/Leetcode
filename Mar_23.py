'''
#######################
# 13. Roman to Integer
#######################
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        t = 0
        for i in range (len(s)-1):
            if roman[s[i]]<roman[s[i+1]]:
                t -= roman[s[i]]
            else:
                t += roman[s[i]]
        return t+roman[s[-1]]
s = 'MCMXCVI'
solu = Solution()
print (solu.romanToInt(s))
'''
'''
############################
# 14. Longest Common Prefix
############################
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        l = 0
        for i in zip(*strs):
            l = l+1
            if len(set(i)) > 1:
                return strs[0][:(l-1)]
        return strs[0][:l]


strs = ['']
solu = Solution()
print (solu.longestCommonPrefix(strs))
'''
'''
##########################################
# 26. Remove Duplicates from Sorted Array
##########################################
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        slow = 1
        for i in range (1, len(nums)):
            if nums[i] > nums[slow]:
                nums[i], nums[slow] = nums[slow], nums[i]            
            if nums[slow] > nums[slow-1]:
                slow += 1
        return len(nums[:slow])
nums = [1,1,2]
solu = Solution()
print (solu.removeDuplicates(nums))
'''
'''
#########################
# 28. Implement strStr()
#########################
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not (haystack or needle):
            return 0
        if not haystack:
            return -1
        for i in range (len(haystack)):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1
haystack = "lkkkkk"
needle = "k"
solu = Solution()
print (solu.strStr(haystack,needle))
'''
'''
#########################
# 38. Count and Say
#########################
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range (n-1):
            s = self.countnumber(s)
        return s


    def countnumber(self,m):
        count = 1
        temp = []
        for i in range (1, len(m)):
            if m[i] == m[i-1]:
                count += 1
            else:
                t = str(count) + str(m[i-1])
                count = 1
                temp.append(t)
        t = str(count) + str(m[-1])
        temp.append(t)
        return ''.join(temp)         
n = 3
solu = Solution()
print (solu.countAndSay(n))

############ regular expression #############
import re
s = '23222322'
q = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
# q = re.sub(r'(.)(.)\1*', 'ha', s)
# print (re.search(r'(.)(.)\1*', s).group(0))
# print (q)
'''












