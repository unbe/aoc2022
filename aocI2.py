cubes=[]

with open("input.txt", "r") as f:
    for _, line in enumerate(f):
        cubes.append(tuple(int(x) for x in line.strip().split(',')))

zop = list(zip(*cubes))
maxs = tuple(max(d) for d in zop)
mins = tuple(min(d) for d in zop)

cubes = frozenset(cubes)

dd = []
for x in (-1, 0, 1):
  for y in (-1, 0, 1):
    for z in (-1, 0, 1):
      if abs(x) + abs(y) + abs(z) == 1:
        dd.append((x,y,z))

def flood(start_cube):
    if start_cube in cubes:
        return([], False)
    water = False
    visited=set([start_cube])
    q=[start_cube]
    while len(q) > 0:
        cube = q.pop()
        visited.add(cube)
        for d in dd:
          nei = tuple(sum(x) for x in zip(cube,d))
          if nei in visited:
              continue
          if nei in cubes:
              continue
          if any(a < b for a,b in zip(cube, mins)):
              water = True
              continue
          if any(a > b for a,b in zip(cube, maxs)):
              water = True
              continue
          q.append(nei)
    return(visited, water)

known = {}
def water(start):
    if start in known:
        water = known[start]
    else:
        connected, water = flood(start)
        for x in connected:
            known[x] = water
    return water

surface = 0
for cube in cubes:
  for d in dd:
    nei = tuple(sum(x) for x in zip(cube,d))
    if water(nei):
      surface += 1
  
print(surface)
