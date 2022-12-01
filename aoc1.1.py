
with open("input.txt", "r") as f:
  elfsum = 0
  most = 0
  for _, line in enumerate(f):
    line = line.strip()
    if line == "":
      most = max(most, elfsum)
      elfsum = 0
    else:
      elfsum += int(line)

print(most)
