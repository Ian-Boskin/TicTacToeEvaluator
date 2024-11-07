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
        count, win, nextMove = Max(board)
    else:
        count, win, nextMove = Min(board)

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
        return 1, -1, board
    if win == 0:
        return 1, 0, board
    maxNode = -1
    nodeCount = 0
    nextMove = (0,0)
    nextCount = sys.maxsize
    for row in range(4):
        for piece in range(4):
            if board[row][piece] == '-':
                board[row][piece] = 'X'
                count, newNode, newCopy = Min(board)
                nodeCount += count
                if newNode >= maxNode:
                    if newNode > maxNode:
                        maxNode = newNode
                    if count < nextCount:
                        nextMove = (row, piece)
                        nextCount = count
                board[row][piece] = '-'

    return nodeCount, maxNode, nextMove

def Min(board):
    win = winState(board, 'X')
    if win == 1:
        return 1, 1, board
    if win == 0:
        return 1, 0, board
    minNode = 1
    nodeCount = 1
    nextMove = (0,0)
    nextCount = sys.maxsize
    for row in range(4):
        for piece in range(4):
            if board[row][piece] == '-':
                board[row][piece] = 'O'
                count, newNode, newCopy = Max(board)
                nodeCount += count
                if newNode <= minNode:
                    if newNode < minNode:
                        minNode = newNode
                    if count < nextCount:
                        nextMove = (row, piece)
                        nextCount = count
                board[row][piece] = '-'

    return nodeCount, minNode, nextMove


main()