from collections import defaultdict
import random
class Node:
    def __init__(self, state):
        self.state = state
        self.children = defaultdict()
        self.par = None

with open('adjX.txt','w'): pass
file = open('adjX.txt','w')

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
    if dotCount==1 and oCount==2:
        return dotPos
    if oCount==3:
        return 'O'
    elif xCount==3:
        return 'X'
    
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
board = [['.' for i in range(3)] for j in range(3)]
root = Node(tup(board))
def allPossibleOutcomes(board, turn, cur):
    global root
    win = findWinner(board)
    if win != None:
        r = root
        for state in cur[1:]:
            if not state in r.children:
                r.children[state] = Node(state)
            r.children[state].par = r
            r = r.children[state]
        return
    f = True
    for i in range(3):
        for j in range(3):
            if board[i][j]=='.':
                f = False
                break
    if f:
        r = root
        for state in cur[1:]:
            if not state in r.children:
                r.children[state] = Node(state)
            r = r.children[state]
        return
    if turn%2==0:
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = 'X'
                    allPossibleOutcomes(board, turn+1, cur + [tup(board)])
                    board[i][j] = '.'
                    
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                    allPossibleOutcomes(board, turn+1, cur + [tup(board)])
                    board[i][j] = '.'

allPossibleOutcomes(board, 0, [tup(board)])


def canWin(node, p):
    if findWinner(node.state)==p:
        return True
    for v in node.children:
        if canWin(node.children[v], p):
            return True
    return False

def onlyWin(node, p):
    if len(node.children)==0 and findWinner(node.state)!=p:
        return False
    for v in node.children:
        if not onlyWin(node.children[v], p):
            return False
    return True

def hasMissingLeaf(node):
    if len(node.children)==0:
        if findWinner(node.state)==None:
            for i in node.state:
                for j in i:
                    if j=='.':
                        return True
        return False
    for v in node.children:
        if hasMissingLeaf(node.children[v]):
            return True
    return False


def traverse(node, depth):
    for v in list(node.children.keys()):
        if v in node.children:
            traverse(node.children[v], depth+1)
    if depth%2 == 1:
        if canWin(node, 'O'):
            if node.state in node.par.children:
                del node.par.children[node.state]
        elif onlyWin(node, 'X'):
            node.par.children = defaultdict()
            node.par.children[node.state] = node
        if hasMissingLeaf(node):
            if node.state in node.par.children:
                del node.par.children[node.state]

traverse(root, 0)

adj = defaultdict(set)

def preorder(node):
    global adj
    for v in node.children:
        adj[node.state].add(v)
        preorder(node.children[v])

preorder(root)

file.write(str(adj))

def play():
    global adj
    global root
    turn = 0
    board = [['.' for i in range(3)] for j in range(3)]
    display(board)
    r = root
    while turn < 5:
        try:
            print(len(list(r.children.keys())), list(r.children.keys()))
            r = r.children[random.choice(list(r.children.keys()))]
            board = clone(r.state)
        except:
            print("Draw / Invalid decesion tree")
            print(r.state)
            print(r.children)
        print("Comp move: ")
        display(board)
        win = findWinner(board)
        if win != None:
            print(win,"Wins !")
            break
        x,y = map(int,input("enter pos: ").split())
        while x <= 0 or y <= 0 or x>3 or y>3 or board[x-1][y-1] != '.':
            print("Already occupied / Invalid position")
            x,y = map(int,input("enter pos: ").split())
        board[x-1][y-1] = 'O'
        r = r.children[tup(board)]
        board = clone(r.state)
        display(board)
        win = findWinner(board)
        if win != None:
            print(win,"Wins !")
            break
        turn += 1

play()