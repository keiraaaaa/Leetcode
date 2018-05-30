'''
#########################
# 283. Move Zeros
#########################
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        z = 0
        for i in range (len(nums)):
            if nums[i] != 0:
                nums[i], nums[z] =  nums[z], nums[i]
                z = z + 1
'''
'''
#########################
# 437. Path Sum III
#########################
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root:
            return self.findpath(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0

    def findpath(self, root, target):
        if root:
            return int(root.val == target) + self.findpath(root.left, target-root.val) + self.findpath(root.right, target-root.val)
        return 0
'''
'''
#####################################
# 438. Find All Anagrams in a String
#####################################
from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s)>=len(p):
            sdict = {}
            pdict = {}
            l = []
            for i in range (len(p)):
                if p[i] in pdict:
                    pdict[p[i]] += 1
                else:
                    pdict[p[i]] = 1
            print (sdict)
            for i in range (len(p)-1):
                if s[i] in sdict:
                    sdict[s[i]] += 1
                else:
                    sdict[s[i]] = 1
            print (sdict)
            for i in range (len(p)-1,len(s)):
                if s[i] in sdict:
                    sdict[s[i]] += 1
                else:
                    sdict[s[i]] = 1
                if sdict == pdict:
                    print (i-len(p)+1)
                    l.append(i-len(p)+1)
                if sdict[s[i-len(p)+1]]==1:
                    sdict.pop(s[i-len(p)+1])
                else:
                    sdict[s[i-len(p)+1]] -= 1
        else:
            l = []
        return l

s = 'abab'
p = 'ab'
'''
'''
################################################
# 448. Find All Numbers Disappeared in an Array
################################################
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range (len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        a = []

        for i in range (len(nums)):
            if nums[i] > 0:
                a.append(i+1)
        return a
solu = Solution()
input = [4,3,2,7,8,2,3,1]
print (solu.findDisappearedNumbers(input))
'''
########################
# 461. Hamming Distance
########################
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        count = 0
        while xor:
            count += xor & 1
            print (xor)
            xor = xor >> 1
        return count

x = 1
y = 20
solu = Solution()
print (solu.hammingDistance(x,y))







