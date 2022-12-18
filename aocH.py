with open("input.txt", "r") as f:
    moves = f.readline().strip()

rocks = [
"""
..@@@@.
""",
"""
...@...
..@@@..
...@...
""",
"""
....@..
....@..
..@@@..
""",
"""
..@....
..@....
..@....
..@....
""",
"""
..@@...
..@@...
""",
]

chamber = """
.......
.......
.......
.......
#######
"""

def noel(text):
    return [list(z) for z in text.split('\n') if z != ""]

def coords(rock):
    r = []
    for y, line in enumerate(rock):
        for x, ch in enumerate(line):
            if ch != '.':
                r.append((x,y))
    return r;


def sho(chamber, rock):
    r = ""
    for y, line in enumerate(chamber):
        for x, ch in enumerate(line):
            r += "@" if rock is not None and (x,y) in rock else ch
        r += "\n"
    return r

chamber = noel(chamber)
rocks = [coords(noel(r)) for r in rocks]

mptr = 0
rptr = 0
rock = rocks[rptr][:]

def fits(rock, chamber):
    for x,y in rock:
        if x<0 or y<0 or y >= len(chamber) or x >= len(chamber[y]):
            return False
        if chamber[y][x] != '.':
            return False
    return True

def peak(chamber):
  for y, line in enumerate(chamber):
    if '#' in line:
      miny = y
      break
  return len(chamber) - miny - 1  # floor doesn't count

rcnt = 0
profiles = {}

limit = 1000000000000   # 2022 for part1
foldup = 0

while True:
    move = moves[mptr]
    mptr = (mptr + 1) % len(moves)
    dx = -1 if move == '<' else 1
    dy = 0
    moved_rock = [(r[0] + dx, r[1] + dy) for r in rock]
    if fits(moved_rock, chamber):
        rock = moved_rock

    dx = 0
    dy = 1
    fallen_rock = [(r[0] + dx, r[1] + dy) for r in rock]
    if fits(fallen_rock, chamber):
        rock = fallen_rock
    else:
        for x,y in rock:
            chamber[y][x] = '#'

        rcnt += 1
        if rcnt == limit:
            print(foldup + peak(chamber))
            break

        rptr = (rptr + 1) % len(rocks)
        rock = rocks[rptr][:]

        add = 5 + max((r[1] for r in rock)) - len(chamber) + peak(chamber)
        while add > 0:
          chamber = [['.']*len(chamber[0])] + chamber
          add -= 1
        while add < 0:
          chamber = chamber[1:]
          add += 1

        profile = [1000000000]*len(chamber[0])
        for y, line in enumerate(chamber):
            if max(profile) < 1000000000:
                break
            for x, ch in enumerate(line):
                if ch == '#' and y < profile[x]:
                    profile[x] = y
        profile = (tuple(profile), mptr, rptr)
        if profile in profiles:
            skip = rcnt - profiles[profile][0]
            buildup = peak(chamber) - profiles[profile][1]
            cycles = (limit - rcnt)//skip
            foldup += buildup * cycles
            rcnt += skip * cycles

        profiles[profile] = (rcnt, peak(chamber))

