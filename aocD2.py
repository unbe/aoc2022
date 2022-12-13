import json
import functools

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
    

lst = [[[2]], [[6]]]
with open("input.txt", "r") as f:
  for _, line in enumerate(f):
    if line == "\n":
      continue
    lst.append(json.loads(line))


lst = ["Yes, this is dog"] + sorted(lst, key=functools.cmp_to_key(cmp), reverse=True)
print(lst.index([[2]]) * lst.index([[6]]))

