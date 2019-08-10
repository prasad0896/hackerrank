import collections
def solution():
    board = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
    
    def checker(row):
        print("checking",row)
        count = collections.Counter(row)
        for i in count.keys():
            if count[i] > 1 and i != ".":
                return False
        return True
    boxes = [[] for i in range(9)]
    for i in range(0,9):
        r, c = [], []
        for j in range(0,9):
            r.append(board[i][j])
            c.append(board[j][i])
            box_index = (i//3)*3 + j//3
            boxes[box_index].append(board[i][j])
        if not checker(r) and not checker(c):
            return False
    for i in range(9):
        if not checker(boxes[i]):
            return False
    return True
solution()
