dirs = {
  'U': [1, 0],
  'D': [-1,0],
  'L': [0, -1],
  'R': [0, 1]
}
tailpos=set()
with open("input.txt", "r") as f:
    rope = [[0,0] for x in range(10)]
    tailpos.add(tuple(rope[-1]))
    for _, line in enumerate(f):
      d, n = line.strip().split(' ', 2)
      for _ in range(int(n)):
        rope[0][0] += dirs[d][0];
        rope[0][1] += dirs[d][1];
        for knot in range(len(rope) - 1):
          dist = [x[0] - x[1] for x in zip(rope[knot], rope[knot+1])];
          if any([abs(x) > 1 for x in dist]):
            for idx, dd in enumerate(dist):
              if dd != 0:
                rope[knot+1][idx] += dd//abs(dd)
          tailpos.add(tuple(rope[-1]))

print(len(tailpos))
        

