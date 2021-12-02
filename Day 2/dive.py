arr = []
f = open("input.txt", "r")
for l in f.readlines():
    arr.append(l.strip())

depth = 0
horizontal = 0
# arr = []
print(arr)

# Part 1
for i in arr:
    word, num = i.split(" ")
    if word == "forward":
        horizontal += int(num)

    if word == "down":
        depth += int(num)

    if word == "up":
        depth -= int(num)

print(depth * horizontal)


# Part 2
depth = 0
horizontal = 0
aim = 0

for i in arr:
    word, num = i.split(" ")
    num = int(num)
    if word == "forward":
        horizontal += int(num)
        depth += aim * int(num)

    if word == "down":
        aim += int(num)

    if word == "up":
        aim -= int(num)

print(depth * horizontal)
