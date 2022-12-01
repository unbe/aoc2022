
with open("input.txt", "r") as f:
  elfsum = 0
  top3 = [0,0,0]
  for _, line in enumerate(f):
    line = line.strip()
    if line == "":
      top3.append(elfsum)
      top3 = sorted(top3)[1:]
      elfsum = 0
    else:
      elfsum += int(line)

print(sum(top3))
