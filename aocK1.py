from sortedcontainers import SortedList

inp = []

with open("input.txt", "r") as f:
    for idx, line in enumerate(f):
        inp.append((idx * 10, int(line)))

sl = SortedList(inp)

for i in inp:
    oidx = sl.index(i)
    sl.remove(i)
    idx = (oidx + i[1]) % len(sl)
    if idx > 0:
        newpos = (sl[idx - 1][0] + sl[idx][0]) / 2
    else:
        newpos = sl[idx][0] - 1
    sl.add((newpos, i[1]))

zero = None
for idx, x in enumerate(sl):
    if x[1] == 0:
        zero = idx
        break

print('Zero at', zero)
ll = len(sl)
print(
    sl[(zero + 1000) % ll][1] +
    sl[(zero + 2000) % ll][1] +
    sl[(zero + 3000) % ll][1]
    )
