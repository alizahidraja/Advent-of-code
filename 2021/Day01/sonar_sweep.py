arr = []
f = open("input.txt", "r")
for l in f.readlines():
    arr.append(int(l.strip()))

# arr = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
# print(arr)

# Part 1
count = 0
for i in range(1, len(arr)):
    # print(i)
    prev = arr[i - 1]
    curr = arr[i]
    if curr > prev:
        count += 1
print(count)


# Part 2
count = 0
for i in range(1, len(arr) - 2):
    # print(i)
    prev = sum(arr[i - 1 : i + 2])
    curr = sum(arr[i : i + 3])
    if curr > prev:
        count += 1

print(count)
