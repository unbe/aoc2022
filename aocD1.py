import json

count = 0
def cmp(a, b):
  if type(a) == int and type(b) != int:
    a = [a]
  if type(a) != int and type(b) == int:
    b = [b]
  if type(a) == list:
    for aa, bb in zip(a,b):
      t = cmp(aa, bb)
      if t != 0:
        return t
    return cmp(len(a), len(b))
  if a == b:
    return 0
  if a < b:
    return 1
  return -1
    

with open("input.txt", "r") as f:
  idx = 0
  while True:
      one = json.loads(f.readline())
      two = json.loads(f.readline())
      idx += 1
      if cmp(one, two) > 0:
        count += idx

      if (f.readline() == ""):
        break

print(count)
