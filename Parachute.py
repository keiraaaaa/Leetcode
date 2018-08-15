# function checkTicTacToe(board) { 
#  return null; 
# }

def checkTicTacToe(board):
    if not board: return
    count = 0
    l = len(board)
    j = 0
    k = "*"
    while j<l:
        c = 0
        for i in range (l):
            if i==0 and board[i][j]!=0:
                k = board[i][j]
                c = 1
            if board[i][j]==0:
                count += 1
            if board[i][j]==k and i!=0:
                c += 1
        if c==l: return k
        j += 1
        k = "*"
    i = 0
    k = "*"
    while i<l:
        c = 0
        for j in range (l):
            if j==0 and board[i][j]!=0:
                k = board[i][j]
                c = 1
            if board[i][j]==0:
                count += 1
            if board[i][j]==k and j!=0:
                c += 1
        if c==l: return k 
        i += 1
        k = "*"
    i, j = 0, 0
    if board[0][0]!=0:
        while i<l:
            if board[i][j]==board[0][0]:
                i += 1
                j += 1
            else:
                break
    if i==l: return board[0][0]
    i, j = 0, l-1
    if board[0][l-1]!=0:
        while i<l:
            if board[i][j]==board[0][l-1]:
                i += 1
                j -= 1
            else:
                break
    if i==l: return board[0][l-1]
    return  2 if count==0 else 0

board = [[-1, -1, 1], 
[1, -1, -1], 
[1, 0, -1]]
print (checkTicTacToe(board))