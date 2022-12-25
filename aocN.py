import math
elves = set()

with open("input.txt", "r") as f:
  for y, line in enumerate(f):
    for x, ch in enumerate(line.strip()):
      if ch == '#':
          elves.add((x,y))

rules = [
        ((-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (0, 0)),  
        ((-1, -1), (0, -1), (1, -1), (0, -1)),  
        ((-1, 1), (0, 1), (1, 1), (0, 1)),
        ((-1, -1), (-1, 0), (-1, 1), (-1, 0)),
        ((1, -1), (1, 0), (1, 1), (1, 0)),
]

rounds = 0
while True:
    rounds += 1
    props = {}
    for elf in elves:
        for r in rules:
            app = [tuple((c0 + c1 for c0, c1 in zip(cond, elf))) for cond in r]
            if all(cond not in elves for cond in app[:-1]):
              dest = app[-1]
              if dest in props:
                  props[dest] = None
              else:
                  props[dest] = elf
              break

    if all(k == v for k, v in props.items()):
        break

    for d, s in props.items():
        if s is not None:
            elves.remove(s)
            elves.add(d)

    rules = [rules[0]] + rules[2:] + [rules[1]]

    if rounds == 10:
        area = math.prod((max(a) - min(a) + 1) for a in zip(*elves))
        print(area - len(elves))

print(rounds)
