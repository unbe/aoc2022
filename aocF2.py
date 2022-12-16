import re
with open("input.txt", "r") as f:
    row_segs = [[] for x in range(4000001)]
    for _, line in enumerate(f):
        mm = re.match(r'Sensor at x=(\S+), y=(\S+): closest beacon is at x=(\S+), y=(\S+)', line)
        sx, sy, bx, by = map(int, mm.group(1,2,3,4))
        print(sx, sy, bx, by)
        dst = abs(sx-bx) + abs(sy-by)
        for approach in range(dst):
            row = sy + approach
            if row > 4000000:
                break
            remaining = dst - approach
            seg = [sx - remaining, sx + remaining]
            row_segs[row].append(seg)
        for approach in range(dst):
            row = sy - approach
            if row < 0:
                break
            remaining = dst - approach
            seg = [sx - remaining, sx + remaining]
            row_segs[row].append(seg)

print('Processing')
for x in range(4000001):
    segs = row_segs[x]
    segs = sorted(segs, key = lambda seg: seg[0])
    i = 0
    while i < len(segs) - 1:
        if segs[i][1] < segs[i+1][0]:
            i += 1
            continue
        segs[i][1] = max(segs[i][1], segs[i+1][1])
        segs.pop(i+1)
    for i in range(len(segs)):
        if segs[i][0] > 0:
            print(x, segs)
            print(x + 4000000 * (segs[i][0]-1))
        if segs[i][1] < 4000000:
            print(x, segs)
            print(x + 4000000 * (segs[i][1]+1))
