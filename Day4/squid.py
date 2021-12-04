import numpy as np

arr = []
f = open("input.txt", "r")
for l in f.readlines():
    arr.append(l.strip())
    print(l.strip())


actual = []
for i in arr[0].split(","):
    actual.append(i)

print(actual)

arr = []
f = open("input.txt", "r")
for l in f.readlines():
    arr.append(l.strip())
    print(l.strip())
B = []
won = []
line = 0
for i in range(1, len(arr)):
    X = arr[i].split(" ")
    if len(X) < 5:
        continue
    # print(B, X)
    B.append([])
    for j in X:
        if len(j) > 0:
            B[line - 1].append(j)
    line += 1


print(B)
BOARD = [[]]
ind = 0
count = 0
for i in B:
    for j in i:
        BOARD[ind].append(j)
        count += 1
    if count == 25:
        ind += 1
        count = 0
        BOARD.append([])

BOARD.pop()
print(BOARD)
print()


def winner(board):
    n = 5
    board = np.array(board).reshape(5, 5)
    # print(board)
    a = ["YES", "YES", "YES", "YES", "YES"]
    if (board == a).all(axis=1).any():
        return True
    if (board == a).all(axis=0).any():
        return True
    return False


def ceckrowcol(B, curr):
    ind = -1
    for board in range(len(B)):
        for x in range(len(B[board])):
            if B[board][x] in curr:
                B[board][x] = "YES"
        if winner(B[board]):
            ind = board
            return B, ind

    # print(B)
    # print()
    return B, ind


curr = []
start = 0
WIN = 0
while True:
    if start == 0:
        for x in actual[:5]:
            curr.append(x)
        start += 1
    elif start == 1:
        for x in actual[5:11]:
            curr.append(x)
        start += 1
    else:
        curr.append(actual[9 + start])
        start += 1

    BOARD, INDEX = ceckrowcol(BOARD, curr)
    print(start, curr)
    if INDEX >= 0:
        break

print(INDEX, actual[9 + start - 1])
sum = 0
for i in BOARD[INDEX]:
    try:
        sum += int(i)
    except:
        pass

print("Ans, Part1:", sum * int(actual[9 + start - 1]))


ll = [x for x in open("input.txt").read().strip().split("\n")]

numbers = ll[0]
boards = [
    [y.split() for y in x.split("\n")]
    for x in open("input.txt").read().strip().split("\n\n")
][1:]


def checkwin(board):
    for i in range(5):
        works = True
        for j in range(5):
            if board[i][j] is not None:
                works = False
        if works:
            return True
    for i in range(5):
        works = True
        for j in range(5):
            if board[j][i] is not None:
                works = False
        if works:
            return True
    return False


won = set()

for number in numbers.split(","):
    for k in range(len(boards)):
        board = boards[k]
        for line in board:
            for i in range(len(line)):
                if line[i] == number:
                    line[i] = None
        if checkwin(board) and (k not in won):
            un = 0
            for line in board:
                for x in line:
                    if x is not None:
                        un += int(x)
            print(un * int(number))
            won.add(k)

print("^answer part 2^")
