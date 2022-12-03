def unit_score(a):
    if a >= 'a' and a <= 'z':
        return 1 + ord(a) - ord('a')
    if a >= 'A' and a <= 'Z':
        return 27 + ord(a) - ord('A')
    raise(a)

with open("input.txt", "r") as f:
    score = 0
    group = []
    for _, line in enumerate(f):
        group.append(set(line.strip()))
        if len(group) == 3:
            badge = set.intersection(*group).pop()
            score += unit_score(badge)
            group = []

print(score)
