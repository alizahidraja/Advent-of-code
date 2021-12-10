arr = []
f = open("input.txt", "r")
for l in f.readlines():
    arr.append(l.strip())


gamma = ""
epsi = ""
binary = ""
temp = [""] * len(arr[0])
for i in arr:
    for j in range(len(arr[0])):
        temp[j] += i[j : j + 1]

for i in temp:
    if i.count("1") > i.count("0"):
        gamma += "1"
        epsi += "0"
    else:
        gamma += "0"
        epsi += "1"

# print(gamma, epsi)
print(int(gamma, 2) * int(epsi, 2))


oxy = ""
co2 = ""

oxy = []
co2 = []

for i in arr:
    oxy.append(i)
for i in range(len(temp)):
    if temp[i].count("1") >= temp[i].count("0"):
        to_rem = []
        for j in oxy:
            if j[i] == "0":
                to_rem.append(j)
        for j in to_rem:
            if j in oxy:
                oxy.remove(j)

    else:
        to_rem = []
        for j in oxy:
            if j[i] == "1":
                to_rem.append(j)
        for j in to_rem:
            if j in oxy:
                oxy.remove(j)
    if len(oxy) == 1:
        break

    temp = [""] * len(oxy[0])
    for i in oxy:
        for j in range(len(oxy[0])):
            temp[j] += i[j : j + 1]


for i in arr:
    co2.append(i)
for i in range(len(temp)):
    if temp[i].count("1") >= temp[i].count("0"):
        to_rem = []
        for j in co2:
            if j[i] == "1":
                to_rem.append(j)
        for j in to_rem:
            if j in co2:
                co2.remove(j)

    else:
        to_rem = []
        for j in co2:
            if j[i] == "0":
                to_rem.append(j)
        for j in to_rem:
            if j in co2:
                co2.remove(j)
    if len(co2) == 1:
        break

    temp = [""] * len(co2[0])
    for i in co2:
        for j in range(len(co2[0])):
            temp[j] += i[j : j + 1]

print(int(oxy[0], 2) * int(co2[0], 2))
