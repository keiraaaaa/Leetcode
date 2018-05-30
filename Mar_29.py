'''
############################################
# 123. Best Time to Buy and Sell Stock III
############################################
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        buy1, sell1, buy2, sell2 = -prices[0], 0, -prices[0], 0

        for price in prices:
            print (price)
            sell2 = max(buy2+price, sell2)         
            buy2 = max(buy2, sell1-price)
            print (sell2,buy2)
            sell1 = max(sell1, buy1+price)
            buy1 = max(buy1, -price)
            print (sell1,buy1)
        return sell2            

prices = [1, 3, 4, 8]
solu = Solution()
print (solu.maxProfit(prices))
'''
'''
############################################
# 188. Best Time to Buy and Sell Stock IV
############################################
class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        if k>=len(prices)/2:
            total = 0
            for i in range(1, len(prices)):
                total += (prices[i] - prices[i-1]) * int(prices[i]>prices[i-1]) 
            return total
        grid = [[-prices[0],0] for i in range (k)] # buy/sell
        if not grid:
            return 0
        for price in prices:
            grid[0][1] = max(grid[0][1], grid[0][0] + price)
            grid[0][0] = max(grid[0][0], -price)            
            for i in range(1,k):
                grid[i][1] = max(grid[i][1], grid[i][0] + price)
                grid[i][0] = max(grid[i][0], grid[i-1][1]-price)
        return grid[k-1][1]
prices = [1, 3, 4, 8]
k = 3
solu = Solution()
print (solu.maxProfit(k,prices))
'''
'''
#########################
# 125. Valid Palindrome
#########################
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        i,j = 0,len(s)-1
        while i < j:
            while i < len(s) and not s[i].isalnum():
                i += 1
            while j>=0 and not s[j].isalnum():
                j -= 1
            if i<j and s[i].lower() != s[j].lower():
                return False
            i += 1; j -= 1
        return True

s = "a."
solu = Solution()
print (solu.isPalindrome(s))
'''
'''
##################################
# 171. Excel Sheet Column Number
##################################
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s:
            total = 0
            for i in range(len(s)):
                total += 26**(len(s)-1-i) * (ord(s[i])-64)
            return total

solu = Solution()
s = 'AAA'
print (solu.titleToNumber(s))
from functools import reduce
print (reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(s)]))
'''
'''
#################################
# 172. Factorial Trailing Zeroes
#################################
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n== 0 else n//5 + self.trailingZeroes(n//5)
n = 10
solu = Solution()
print (solu.trailingZeroes(n))
'''
'''
#####################
# 189. Rotate Array
#####################
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums:
            nums[:] = nums[(len(nums)-k):] + nums[:(len(nums)-k)]      
        return (nums)
nums = [1,2,3,4,5,6,7]
k = 3
solu = Solution()
print (solu.rotate(nums, k))
'''
'''
####################
# 190. Reverse Bits
####################
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int('{:032b}'.format(n)[::-1],2)

n = 43261596
print ('{:032b}'.format(n))
print (int('{:032b}'.format(n)[::-1],2))
'''
'''
########################
# 191. Number of 1 Bits
########################
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        string = '{:032b}'.format(n)
        i = 0
        for s in string:
            i += int(s) & 1
        return i
n = 11
solu = Solution()
print (solu.hammingWeight(n))
'''














