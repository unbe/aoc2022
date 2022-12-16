import re
with open("input.txt", "r") as f:
    row = 2000000
    segs = []
    for _, line in enumerate(f):
        mm = re.match(r'Sensor at x=(\S+), y=(\S+): closest beacon is at x=(\S+), y=(\S+)', line)
        sx, sy, bx, by = map(int, mm.group(1,2,3,4))
        dst = abs(sx-bx) + abs(sy-by)
        approach = abs(sy-row)
        if approach > dst:
            continue
        remaining = dst - approach
        seg = [sx - remaining, sx + remaining]
        segs.append(seg)

segs = sorted(segs, key = lambda seg: seg[0])

i = 0
while i < len(segs) - 1:
    if segs[i][1] < segs[i+1][0]:
        i += 1
        continue
    segs[i][1] = max(segs[i][1], segs[i+1][1])
    segs.pop(i+1)

print(sum(s[1]-s[0] for s in segs))
