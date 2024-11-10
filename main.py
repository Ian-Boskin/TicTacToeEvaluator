import sys


def main():
    board = []
    # with open(input("Please input the file name: ")) as file:
    #     for line in file:
    #         board.append(list(line.rstrip()))

    with open("board.txt") as file:
        for line in file:
            board.append(list(line.rstrip()))

    XCount = 0
    OCount = 0
    for row in board:
        XCount += row.count('X')
        OCount += row.count('O')
    #
    # if abs(XCount - OCount) > 1:
    #     return -1

    if XCount == OCount:
        count, win, nextMove = MaxCutoff(board, 5)
    else:
        count, win, nextMove = MinCutoff(board, 5)

    print(count)
    print(win)
    print(nextMove)



def winState(board, player):
    placedPieces = []
    draw = True
    for row in board:
        placed = []
        for piece in range(len(row)):
            if row[piece] == player:
                placed.append(piece + 1)
            if row[piece] == '-':
                draw = False
        if len(placed) == 0:
            return -1
        placedPieces.append(placed)

    if draw: return 0

    if 1 in placedPieces[0]:
        if 2 in placedPieces[1]:
            if 3 in placedPieces[2]:
                if 4 in placedPieces[3]:
                    return 1
            if 4 in placedPieces[2]:
                if 3 in placedPieces[3]:
                    return 1
        if 3 in placedPieces[1]:
            if 2 in placedPieces[2]:
                if 4 in placedPieces[3]:
                    return 1
            if 4 in placedPieces[2]:
                if 2 in placedPieces[3]:
                    return 1
        if 4 in placedPieces[1]:
            if 3 in placedPieces[2]:
                if 2 in placedPieces[3]:
                    return 1
            if 2 in placedPieces[2]:
                if 3 in placedPieces[3]:
                    return 1
    if 2 in placedPieces[0]:
        if 1 in placedPieces[1]:
            if 3 in placedPieces[2]:
                if 4 in placedPieces[3]:
                    return 1
            if 4 in placedPieces[2]:
                if 3 in placedPieces[3]:
                    return 1
        if 3 in placedPieces[1]:
            if 1 in placedPieces[2]:
                if 4 in placedPieces[3]:
                    return 1
            if 4 in placedPieces[2]:
                if 1 in placedPieces[3]:
                    return 1
        if 4 in placedPieces[1]:
            if 3 in placedPieces[2]:
                if 1 in placedPieces[3]:
                    return 1
            if 1 in placedPieces[2]:
                if 3 in placedPieces[3]:
                    return 1
    if 3 in placedPieces[0]:
        if 1 in placedPieces[1]:
            if 2 in placedPieces[2]:
                if 4 in placedPieces[3]:
                    return 1
            if 4 in placedPieces[2]:
                if 2 in placedPieces[3]:
                    return 1
        if 2 in placedPieces[1]:
            if 1 in placedPieces[2]:
                if 4 in placedPieces[3]:
                    return 1
            if 4 in placedPieces[2]:
                if 1 in placedPieces[3]:
                    return 1
        if 4 in placedPieces[1]:
            if 2 in placedPieces[2]:
                if 1 in placedPieces[3]:
                    return 1
            if 1 in placedPieces[2]:
                if 2 in placedPieces[3]:
                    return 1
    if 4 in placedPieces[0]:
        if 1 in placedPieces[1]:
            if 3 in placedPieces[2]:
                if 2 in placedPieces[3]:
                    return 1
            if 2 in placedPieces[2]:
                if 3 in placedPieces[3]:
                    return 1
        if 3 in placedPieces[1]:
            if 1 in placedPieces[2]:
                if 2 in placedPieces[3]:
                    return 1
            if 2 in placedPieces[2]:
                if 1 in placedPieces[3]:
                    return 1
        if 2 in placedPieces[1]:
            if 3 in placedPieces[2]:
                if 1 in placedPieces[3]:
                    return 1
            if 1 in placedPieces[2]:
                if 3 in placedPieces[3]:
                    return 1

    return -1

def possibleWins(board, player):
    placedPieces = []
    for row in board:
        placed = []
        for piece in range(len(row)):
            if row[piece] == player or row[piece] == '-':
                placed.append(piece + 1)
        if len(placed) == 0:
            return 0
        placedPieces.append(placed)

    count = 0

    if 1 in placedPieces[0]:
        if 2 in placedPieces[1]:
            if 3 in placedPieces[2]:
                if 4 in placedPieces[3]:
                    count += 1
            if 4 in placedPieces[2]:
                if 3 in placedPieces[3]:
                    count += 1
        if 3 in placedPieces[1]:
            if 2 in placedPieces[2]:
                if 4 in placedPieces[3]:
                    count += 1
            if 4 in placedPieces[2]:
                if 2 in placedPieces[3]:
                    count += 1
        if 4 in placedPieces[1]:
            if 3 in placedPieces[2]:
                if 2 in placedPieces[3]:
                    count += 1
            if 2 in placedPieces[2]:
                if 3 in placedPieces[3]:
                    count += 1
    if 2 in placedPieces[0]:
        if 1 in placedPieces[1]:
            if 3 in placedPieces[2]:
                if 4 in placedPieces[3]:
                    count += 1
            if 4 in placedPieces[2]:
                if 3 in placedPieces[3]:
                    count += 1
        if 3 in placedPieces[1]:
            if 1 in placedPieces[2]:
                if 4 in placedPieces[3]:
                    count += 1
            if 4 in placedPieces[2]:
                if 1 in placedPieces[3]:
                    count += 1
        if 4 in placedPieces[1]:
            if 3 in placedPieces[2]:
                if 1 in placedPieces[3]:
                    count += 1
            if 1 in placedPieces[2]:
                if 3 in placedPieces[3]:
                    count += 1
    if 3 in placedPieces[0]:
        if 1 in placedPieces[1]:
            if 2 in placedPieces[2]:
                if 4 in placedPieces[3]:
                    count += 1
            if 4 in placedPieces[2]:
                if 2 in placedPieces[3]:
                    count += 1
        if 2 in placedPieces[1]:
            if 1 in placedPieces[2]:
                if 4 in placedPieces[3]:
                    count += 1
            if 4 in placedPieces[2]:
                if 1 in placedPieces[3]:
                    count += 1
        if 4 in placedPieces[1]:
            if 2 in placedPieces[2]:
                if 1 in placedPieces[3]:
                    count += 1
            if 1 in placedPieces[2]:
                if 2 in placedPieces[3]:
                    count += 1
    if 4 in placedPieces[0]:
        if 1 in placedPieces[1]:
            if 3 in placedPieces[2]:
                if 2 in placedPieces[3]:
                    count += 1
            if 2 in placedPieces[2]:
                if 3 in placedPieces[3]:
                    count += 1
        if 3 in placedPieces[1]:
            if 1 in placedPieces[2]:
                if 2 in placedPieces[3]:
                    count += 1
            if 2 in placedPieces[2]:
                if 1 in placedPieces[3]:
                    count += 1
        if 2 in placedPieces[1]:
            if 3 in placedPieces[2]:
                if 1 in placedPieces[3]:
                    count += 1
            if 1 in placedPieces[2]:
                if 3 in placedPieces[3]:
                    count += 1

    return count

def Max(board):
    win = winState(board, 'O')
    if win == 1:
        return 1, -1, (-1,-1)
    if win == 0:
        return 1, 0, (-1,-1)
    maxNode = -1
    nodeCount = 0
    nextMove = (-1,-1)
    # nextCount = sys.maxsize
    for row in range(4):
        for piece in range(4):
            if board[row][piece] == '-':
                board[row][piece] = 'X'
                count, newNode, newCopy = Min(board)
                nodeCount += count
                if newNode > maxNode:
                    maxNode = newNode
                    nextMove = (row, piece)
                #     nextCount = count
                # elif newNode == maxNode and count < nextCount:
                #     nextMove = (row, piece)
                #     nextCount = count
                board[row][piece] = '-'

    return nodeCount, maxNode, nextMove

def Min(board):
    win = winState(board, 'X')
    if win == 1:
        return 1, 1, (-1,-1)
    if win == 0:
        return 1, 0, (-1,-1)
    minNode = 1
    nodeCount = 1
    nextMove = (0,0)
    # nextCount = sys.maxsize
    for row in range(4):
        for piece in range(4):
            if board[row][piece] == '-':
                board[row][piece] = 'O'
                count, newNode, newCopy = Max(board)
                nodeCount += count
                if newNode < minNode:
                    minNode = newNode
                    nextMove = (row, piece)
                #     nextCount = count
                # elif newNode == minNode and count < nextCount:
                #     nextMove = (row, piece)
                #     nextCount = count
                board[row][piece] = '-'

    return nodeCount, minNode, nextMove

def MaxCutoff(board, k):
    win = winState(board, 'O')
    if win == 1:
        return 1, -100, (-1,-1)
    if win == 0:
        return 1, 0, (-1,-1)
    if k == 0:
        Xwins = possibleWins(board, 'X')
        Owins = possibleWins(board, 'O')
        return 1, Xwins-Owins, (-1,-1)
    maxNode = -100
    nodeCount = 0
    nextMove = (-1,-1)
    # nextCount = 0
    for row in range(4):
        for piece in range(4):
            if board[row][piece] == '-':
                board[row][piece] = 'X'
                count, newNode, newCopy = MinCutoff(board , k-1)
                nodeCount += count
                if newNode > maxNode:
                    maxNode = newNode
                    nextMove = (row, piece)
                #     nextCount = count
                # elif newNode == maxNode and count > nextCount:
                #     nextMove = (row, piece)
                #     nextCount = count
                board[row][piece] = '-'

    return nodeCount, maxNode, nextMove

def MinCutoff(board, k):
    win = winState(board, 'X')
    if win == 1:
        return 1, 100, (-1,-1)
    if win == 0:
        return 1, 0, (-1,-1)
    if k == 0:
        Xwins = possibleWins(board, 'X')
        Owins = possibleWins(board, 'O')
        return 1, Xwins-Owins, (-1,-1)
    minNode = 100
    nodeCount = 1
    nextMove = (0,0)
    # nextCount = 0
    for row in range(4):
        for piece in range(4):
            if board[row][piece] == '-':
                board[row][piece] = 'O'
                count, newNode, newCopy = MaxCutoff(board, k-1)
                # if k == 5:
                #     print(count, newNode, (row, piece), newCopy, sep=' ')
                nodeCount += count
                if newNode < minNode:
                    minNode = newNode
                    nextMove = (row, piece)
                #     nextCount = count
                # elif newNode == minNode and count > nextCount:
                #     nextMove = (row, piece)
                #     nextCount = count
                board[row][piece] = '-'

    return nodeCount, minNode, nextMove


main()