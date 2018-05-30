'''
######################
# 48. Rotate Image
######################
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            l = len(matrix)
            i = 0
            while i < l//2:
                matrix[i], matrix[len(matrix)-i-1] = matrix[len(matrix)-i-1], matrix[i]
                i += 1
            for i in range(l-1):
                for j in range(i+1,l):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

matrix = [[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]
solu = Solution()
print (solu.rotate(matrix))
'''

######################
# 49. Group Anagrams
######################
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for str_ in strs:
            key = ''.join(sorted(str_))
            if key in dic:
                dic[key].append(str_)
            else:
                dic[key] = [str_]
        return list(dic.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solu = Solution()
print (solu.groupAnagrams(strs))













