arr = []
f = open("input.txt", "r")
for l in f.readlines():
    arr.append(l.strip())
    # print(l.strip())


mapp = []
valids = []


for i in arr:
    start, end = i.split("->")
    start = start.strip().split(",")
    end = end.strip().split(",")
    if start[0] == end[0] or start[1] == end[1]:
        valids.append((start, end))

# print(valids)

max = 0
for i in valids:
    # print(i[0])
    if int(i[0][0]) > max:
        max = int(i[0][0])
    if int(i[0][1]) > max:
        max = int(i[0][1])
    if int(i[1][0]) > max:
        max = int(i[1][0])
    if int(i[1][1]) > max:
        max = int(i[1][1])

max += 1
# print(max)


mapp = [[0] * max for _ in range(max)]


for i in valids:
    # print(i)
    if i[0][0] == i[1][0]:
        if int(i[0][1]) < int(i[1][1]):
            for j in range(int(i[0][1]), int(i[1][1]) + 1):

                mapp[j][int(i[0][0])] += 1
        else:
            for j in range(int(i[1][1]), int(i[0][1]) + 1):
                # print(j, int(i[0][0]))
                mapp[j][int(i[0][0])] += 1

    if i[0][1] == i[1][1]:
        if int(i[0][0]) < int(i[1][0]):
            for j in range(int(i[0][0]), int(i[1][0]) + 1):
                # print(int(i[0][1]), j)
                mapp[int(i[0][1])][j] += 1
        else:
            for j in range(int(i[1][0]), int(i[0][0]) + 1):
                # print(int(i[0][1]), j)
                mapp[int(i[0][1])][j] += 1

# for i in range(max):
# for j in range(max):
#    print(mapp[i][j], end="")
# print()

overlapp = 0
for i in range(max):
    for j in range(max):
        if mapp[i][j] > 1:
            overlapp += 1

print("Part 1", overlapp)


mapp = []
valids = []


for i in arr:
    start, end = i.split("->")
    start = start.strip().split(",")
    end = end.strip().split(",")
    valids.append(((int(start[0]), int(start[1])), (int(end[0]), int(end[1]))))

# print(valids)

max = 0
for i in valids:
    if int(i[0][0]) > max:
        max = int(i[0][0])
    if int(i[0][1]) > max:
        max = int(i[0][1])
    if int(i[1][0]) > max:
        max = int(i[1][0])
    if int(i[1][1]) > max:
        max = int(i[1][1])

max += 1
# print(max)


mapp = [[0] * max for _ in range(max)]


for ((x1, y1), (x2, y2)) in valids:
    v = [0, 0]

    if x1 < x2:
        v[0] = 1
    elif x1 > x2:
        v[0] = -1

    if y1 < y2:
        v[1] = 1
    elif y1 > y2:
        v[1] = -1

    while (x1, y1) != (x2, y2):

        mapp[x1][y1] += 1

        x1 += v[0]
        y1 += v[1]

    mapp[x2][y2] += 1


# for i in range(max):
#    for j in range(max):
#        print(mapp[i][j], end="")
#    print()

overlapp = 0
for i in range(max):
    for j in range(max):
        if mapp[i][j] > 1:
            overlapp += 1

print("Part 2", overlapp)
