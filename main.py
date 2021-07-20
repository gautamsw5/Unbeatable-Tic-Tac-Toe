from collections import defaultdict
import random

file = open('adjO.txt','r')
adjO = defaultdict(set)
for line in file:
    pass

line = line[line.index('{')+1:line.rindex('}')]

i = 0
while i < len(line):
    j = line.find(':', i)
    k = line.find('}', i)
    # print(line[i:j])
    # print(line[j+2:k+1])
    # break
    key = eval(line[i:j])
    value = eval(line[j+2:k+1])
    adjO[key] = value
    i = k+3
    # print(key, value)

file = open('adjX.txt','r')
adjX = defaultdict(set)
for line in file:
    pass

line = line[line.index('{')+1:line.rindex('}')]

i = 0
while i < len(line):
    j = line.find(':', i)
    k = line.find('}', i)
    # print(line[i:j])
    # print(line[j+2:k+1])
    # break
    key = eval(line[i:j])
    value = eval(line[j+2:k+1])
    adjX[key] = value
    i = k+3
    # print(key, value)


def findblockPos(board, dct):
    dotCount = 0
    dotPos = None
    xCount = 0
    oCount = 0
    for x in dct:
        if dct[x]=='.':
            dotCount += 1
            dotPos = x
        elif dct[x]=='X':
            xCount += 1
        else:
            oCount += 1
    if dotCount==1 and xCount==2:
        return dotPos
    if xCount==3:
        return 'X'
    elif oCount==3:
        return 'O'
def findOneMoveWin(board, dct):
    dotCount = 0
    dotPos = None
    xCount = 0
    oCount = 0
    for x in dct:
        if dct[x]=='.':
            dotCount += 1
            dotPos = x
        elif dct[x]=='X':
            xCount += 1
        else:
            oCount += 1
    if dotCount==1 and oCount==2:
        return dotPos
def oneMoveWin(board):
    for i in range(3):
        # ith row
        dct = {(i,0):board[i][0], (i,1):board[i][1], (i,2):board[i][2]}
        t = findOneMoveWin(board, dct)
        if t!=None and len(t) > 1:
            board[t[0]][t[1]] = 'O'
            return t
        # ith column
        dct = {(0,i):board[0][i], (1,i):board[1][i], (2,i):board[2][i]}
        t = findOneMoveWin(board, dct)
        if t!=None and len(t) > 1:
            board[t[0]][t[1]] = 'O'
            return t
    # Diagonal
    dct = {(0,0):board[0][0], (1,1):board[1][1], (2,2):board[2][2]}
    t = findOneMoveWin(board, dct)
    if t!=None and len(t) > 1:
        board[t[0]][t[1]] = 'O'
        return t
    # Anti Diagonal
    dct = {(0,2):board[0][2], (1,1):board[1][1], (2,0):board[2][0]}
    t = findOneMoveWin(board, dct)
    if t!=None and len(t) > 1:
        board[t[0]][t[1]] = 'O'
        return t
def blockOtherWin(board):
    for i in range(3):
        # ith row
        dct = {(i,0):board[i][0], (i,1):board[i][1], (i,2):board[i][2]}
        t = findblockPos(board, dct)
        if t!=None and len(t) > 1:
            board[t[0]][t[1]] = 'O'
            return t
        # ith column
        dct = {(0,i):board[0][i], (1,i):board[1][i], (2,i):board[2][i]}
        t = findblockPos(board, dct)
        if t!=None and len(t) > 1:
            board[t[0]][t[1]] = 'O'
            return t
    # Diagonal
    dct = {(0,0):board[0][0], (1,1):board[1][1], (2,2):board[2][2]}
    t = findblockPos(board, dct)
    if t!=None and len(t) > 1:
        board[t[0]][t[1]] = 'O'
        return t
    # Anti Diagonal
    dct = {(0,2):board[0][2], (1,1):board[1][1], (2,0):board[2][0]}
    t = findblockPos(board, dct)
    if t!=None and len(t) > 1:
        board[t[0]][t[1]] = 'O'
        return t
def findWinner(board):
    for i in range(3):
        # ith row
        dct = {(i,0):board[i][0], (i,1):board[i][1], (i,2):board[i][2]}
        t = findblockPos(board, dct)
        if t=='X' or t=='O':
            return t
        # ith column
        dct = {(0,i):board[0][i], (1,i):board[1][i], (2,i):board[2][i]}
        t = findblockPos(board, dct)
        if t=='X' or t=='O':
            return t
    # Diagonal
    dct = {(0,0):board[0][0], (1,1):board[1][1], (2,2):board[2][2]}
    t = findblockPos(board, dct)
    if t=='X' or t=='O':
        return t
    # Anti Diagonal
    dct = {(0,2):board[0][2], (1,1):board[1][1], (2,0):board[2][0]}
    t = findblockPos(board, dct)
    if t=='X' or t=='O':
        return t
def display(board):
    for i in board:
        print(*i)
def clone(board):
    return [[j for j in i] for i in board]
def tup(board):
    return tuple([tuple([j for j in i]) for i in board])

def playO():
    global adjO
    turn = 0
    board = [['.' for i in range(3)] for j in range(3)]
    display(board)
    while turn < 5:
        x,y = map(int,input("enter pos: ").split())
        while x <= 0 or y <= 0 or x>3 or y>3 or board[x-1][y-1] != '.':
            print("Already occupied / Invalid position")
            x,y = map(int,input("enter pos: ").split())
        board[x-1][y-1] = 'X'
        display(board)
        win = findWinner(board)
        if win != None:
            print(win,"Wins !")
            break
        try:
            # board = clone(random.choice(list(adjO[tup(board)])))
            # print("Number of possible moves: ",len(adjO[tup(board)]))
            # print(adjO[tup(board)])
            board = clone(random.choice(list(adjO[tup(board)])))
        except:
            print("Draw game")
            # print(adjO[tup(board)])
            return
        print("Comp move: ")
        display(board)
        win = findWinner(board)
        if win != None:
            print(win,"Wins !")
            break
        turn += 1

def playX():
    global adjX
    turn = 0
    board = [['.' for i in range(3)] for j in range(3)]
    display(board)
    while turn < 5:
        try:
            # board = clone(random.choice(list(adjO[tup(board)])))
            # print("Number of possible moves: ",len(adjO[tup(board)]))
            # print(len(adjX[tup(board)]), adjX[tup(board)])
            board = clone(random.choice(list(adjX[tup(board)])))
        except:
            print("Draw game")
            # print(adjX[tup(board)])
            return
        print("Comp move: ")
        display(board)
        win = findWinner(board)
        if win != None:
            print(win,"Wins !")
            break

        f = True
        for i in board:
            for j in i:
                if j=='.':
                    f = False
                    break
        if f:
            print("Draw game")
            break

        x,y = map(int,input("enter pos: ").split())
        while x <= 0 or y <= 0 or x>3 or y>3 or board[x-1][y-1] != '.':
            print("Already occupied / Invalid position")
            x,y = map(int,input("enter pos: ").split())
        board[x-1][y-1] = 'O'
        display(board)
        win = findWinner(board)
        if win != None:
            print(win,"Wins !")
            break
        turn += 1

while True:
    try:
        p = input("Play as (X/O): ")
        if p=='X' or p=='x':
            playO()
        elif p=='O' or p=='o':
            playX()
    except:
        pass