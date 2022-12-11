import operator
import math

items = []
ops = []
divisors = []
throws = []

def makeop(update):
    if update[1] == '+':
        op = operator.add;
    if update[1] == '*':
        op = operator.mul;
    if update[2] == 'old':
        getarg = lambda old: old
    else:
        getarg = lambda old: int(update[2])
    return lambda old: op(old, getarg(old))

with open("input.txt", "r") as f:
  while True:
    if f.readline() == '':
      break
    items.append([int(x.strip()) for x in f.readline().split(':')[1].split(",")])
    ops.append(makeop(f.readline().split('=')[1].split()))
    divisors.append(int(f.readline().split('by')[1]))
    throws.append([int(f.readline().split()[5]), int(f.readline().split()[5])])
    if f.readline() == '':
      break

inspects = [0] * len(items)
modulus = math.lcm(*divisors)

for round in range(10000):
    for m in range(len(items)):
      for i in range(len(items[m])):
        inspects[m] += 1
        newscore = ops[m](items[m][i]) % modulus
        target = throws[m][0] if (newscore % divisors[m]) == 0 else throws[m][1]
        items[target].append(newscore)
      items[m] = []

mb = sorted(inspects)
print(mb[-1] * mb[-2])
