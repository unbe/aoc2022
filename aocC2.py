import re

mp=[]
q=[]
with open("input.txt", "r") as f:
    score = 0
    for row, line in enumerate(f):
        mp.append(line.strip())
        q += [(row, m.start()) for m in re.finditer('a|S', mp[-1])]
        if 'E' in mp[-1]:
            E  = (row, mp[-1].find('E'))

def h(s):
    if s == 'S':
        s = 'a'
    if s == 'E':
        s = 'z'
    return ord(s)
def move(x, y, nx, ny):
    if nx < 0 or ny < 0 or nx >= len(mp) or ny >= len(mp[0]):
        return
    if h(mp[x][y]) < h(mp[nx][ny]) - 1:
        return
    if dist[nx][ny] <= dist[x][y] + 1:
        return
    dist[nx][ny] = dist[x][y] + 1
    q.append((nx, ny))

dist = [[10**10]*len(mp[0]) for x in range(len(mp))]
for c in q:
  dist[c[0]][c[1]] = 0

while len(q) > 0:
    x, y = q.pop()
    move(x, y, x - 1, y)
    move(x, y, x, y - 1)
    move(x, y, x + 1, y)
    move(x, y, x, y + 1)

print(dist[E[0]][E[1]])
