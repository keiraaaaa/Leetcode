'''
######################
# 36. Valid Sudoku
######################
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        m = []
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    m += [(i,board[i][j]), (board[i][j], j), (i//3, j//3, board[i][j])]
        return len(m)==len(set(m))

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["3",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

solu = Solution()
print (solu.isValidSudoku(board))
'''
'''
######################
# 50. Pow(x, n)
######################
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0: return 1
        if n>0: 
            start = x
        if n<0: 
            start = 1/x
            n = abs(n)
        temp = 1
        out = 1
        while temp<=n:
            num = start
            while (temp<<1)<n:
                num *= num
                temp <<= 1
            out *= num
            n -= temp
            temp = 1
        return out
x = 2.00000
n = -2
solu = Solution()
print (solu.myPow(x, n))
'''
'''
######################
# 54. Spiral Matrix
######################
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        out = []
        while matrix:
            out += matrix[0]
            matrix = matrix[1:]
            if matrix:
                matrix = self.rotate(matrix)
        return out

    def rotate(self, matrix):
        out = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
        l2 = len(matrix[0])
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                out[i][j] = matrix[j][l2-1-i]
        return out

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
# matrix = [
#  [ 1, 2],
#  [ 4, 5],
#  [ 7, 8]
# ]
matrix = [
  []
]
solu = Solution()
print (solu.spiralOrder(matrix))
'''

########################
# 73. Set Matrix Zeroes
########################
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row, column = False, False
        for i in range (len(matrix)):
            for j in range (len(matrix[i])):
                if i==0 and matrix[i][j]==0:
                    row = True
                if j==0 and matrix[i][j]==0:
                    column = True
                if i>0 and j>0 and matrix[i][j]==0:
                    matrix[i][0], matrix[0][j] = 0, 0
        for i in range (len(matrix)-1, -1, -1):
            for j in range (len(matrix[i])-1, -1, -1):
                if (i>0 and j>0) and (matrix[i][0]==0 or matrix[0][j]==0):
                    matrix[i][j] = 0
                if column==True and j==0:
                    matrix[i][j]=0
                if row==True and i==0:
                    matrix[i][j]=0
        return matrix     


matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
solu = Solution()
print (solu.setZeroes(matrix))








