cubes=[]
with open("input.txt", "r") as f:
    for _, line in enumerate(f):
        cubes.append(tuple(int(x) for x in line.strip().split(',')))
cubes = frozenset(cubes)

dd = []
for x in (-1, 0, 1):
  for y in (-1, 0, 1):
    for z in (-1, 0, 1):
      if abs(x) + abs(y) + abs(z) == 1:
        dd.append((x,y,z))

surface = 0
for cube in cubes:
  for d in dd:
    nei = tuple(sum(x) for x in zip(cube,d))
    if nei not in cubes:
      surface += 1
  
print(surface)
