# for string
arr = []
fpath = "c:/Users/Ali Zahid Raja/Desktop/Advent of Code/Advent-of-code-2021/2021/Day17/input.txt"
f = open(fpath, "r")
for l in f.readlines():
    arr.append(l.strip())
    # print(l.strip())

print(arr)
