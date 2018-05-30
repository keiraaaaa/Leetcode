###########
# 1. Two sum
###########
'''
nums = [2,7,11,15]
target = 9
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        c = {}
        for i in range(len(nums)):
        	if nums[i] in c:
        		return [c[nums[i]],i]
        	else:
        		c[target - nums[i]] = i

solu = Solution()
print (solu.twoSum(nums, target))

nums = [2,7,11,15]
c = {5:1}
print (4 in c)
'''

####################
# 20. Valid Parentheses
####################
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict_20 = {')':'(',']':'[','}':'{'}
        for char in s:
        	if char in dict_20.values():
        		stack.append(char)
        	elif char in dict_20.keys():
        		if stack==[] or dict_20[char] != stack.pop():
        			return False
        	else:
        		return False
        return stack == []
s = "[]]"
solu = Solution()
solu.isValid(s)
# print (solu.isValid(s))


c = {5:1,4:3}
k = [1,2,3]
k.pop()==3
print (k)
# print (c.keys())
# print (k.pop())
# print (k)
# s = '()p]'
# for char in s:
# 	print (char)