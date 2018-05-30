#####################
# 62. Unique Paths
#####################
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
'''
# DFS: TLE
        out = []
        self.find(out, m ,n)
        return sum(out)

    def find(self, out, m, n):
        if m==1 or n ==1:
            out.append(1)
            return out
        else:
            self.find(out, m-1, n)
            self.find(out, m, n-1)
'''
        t = [[1]*m for i in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                t[i][j] = t[i-1][j] + t[i][j-1]
        return t[-1][-1]
m = 7
n = 3
solu = Solution()
print (solu.uniquePaths(m,n))
