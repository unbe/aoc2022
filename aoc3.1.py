def unit_score(a):
    if a >= 'a' and a <= 'z':
        return 1 + ord(a) - ord('a')
    if a >= 'A' and a <= 'Z':
        return 27 + ord(a) - ord('A')
    raise(a)

with open("input.txt", "r") as f:
    score = 0
    for _, line in enumerate(f):
        line = line.strip()
        one = line[len(line)/2:]
        two = line[:len(line)/2]
        common = list(set(one).intersection(set(two)))[0]
        score += unit_score(common)

print(score)
