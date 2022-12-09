dirs = {
  'U': [1, 0],
  'D': [-1,0],
  'L': [0, -1],
  'R': [0, 1]
}
tailpos=set()
with open("input.txt", "r") as f:
    H = [0, 0]
    T = [0, 0]
    tailpos.add(tuple(T))
    for _, line in enumerate(f):
      d, n = line.strip().split(' ', 2)
      for _ in range(int(n)):
        H[0] += dirs[d][0];
        H[1] += dirs[d][1];
        dist = [x[0] - x[1] for x in zip(H,T)];
        if any([abs(x) > 1 for x in dist]):
          for idx, dd in enumerate(dist):
            if dd != 0:
              T[idx] += dd//abs(dd)
          tailpos.add(tuple(T))

print(len(tailpos))
        

