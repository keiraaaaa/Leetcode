##############################
# 70. Climbing Stairs
##############################
# # Top down - TLE
# n = 3
# class Solution:
# 	def climbStairs(self, n):
# 	    """
# 	    :type n: int
# 	    :rtype: int
# 	    """
# 	    if n == 1:
# 	    	return 1
# 	    if n == 2:
# 	    	return 2
# 	    return self.climbStairs(n-1)+self.climbStairs(n-2)
# s = Solution()
# print (s.climbStairs(n))

# Bottom up
class Solution:
	def climbStairs(self, n):
	    """
	    :type n: int
	    :rtype: int
	    """
	    if n == 1:
	    	return 1
	    if n == 2:
	    	return 2
	    res = [0 for i in range(n)]
	    res[0] = 1
	    res[1] = 2
	    for i in range (2, n):
	    	res[i] = res[i-1] + res[i-2]
	    return res[-1]
n = 3
s = Solution()
print (s.climbStairs(n))
