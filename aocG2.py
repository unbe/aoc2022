import re
nodes = {}
with open("input.txt", "r") as f:
    for _, line in enumerate(f):
        (valve, flow, exits) = re.match(r'Valve (..) has flow rate=(\d+); tunnels? leads? to valves? ((?:..(?:, |$))+)$', line).groups()
        exits = exits.split(', ')
        nodes[valve] = [int(flow), exits, None]

nodelist = sorted(nodes.keys())
nodei = []
for n in nodelist:
    inode = nodes[n][:]
    inode[1] = [nodelist.index(x) for x in nodes[n][1]]
    nodei.append(inode)

W = [[10**8]*len(nodei) for x in nodei]
for a in range(len(nodei)):
    for b in range(len(nodei)):
        W[a][b] = 1 if b in nodei[a][1] else 10**8

for k in range(len(nodei)):
  for i in range(len(nodei)):
    for j in range(len(nodei)):
      W[i][j] = min(W[i][j], W[i][k]+W[k][j])

for a in range(len(nodei)):
  for b in range(len(nodei)):
    W[a][b] += 1

import functools

@functools.cache
def search(players, tick, visited):
    # fast forward until some players need a choice
    ff = min(p[1] for p in players)
    tick -= ff
    players = tuple((p[0], p[1]-ff) for p in players)
    
    for p in players:
        visited |= 1 << p[0]

    for idx, p in enumerate(players):
        if p[1] == 0:
            advance = idx
            break
    
    nodename = players[advance][0]
    mm = [0, [None]]
    for step in range(len(nodei)):
        if visited & (1<<step):
            continue
        if W[nodename][step] + 1 >= tick:
            continue
        newstate = list(players)
        newstate[advance] = (step, W[nodename][step])
        rstep = search(tuple(sorted(newstate)), tick, visited)
        if rstep[0] > mm[0]:
            mm = rstep
    if mm[1][0] is None:
        flow = sum([(tick-p[1])*nodei[p[0]][0] for p in players if p[1]<tick])
    else:
        flow = nodei[players[advance][0]][0] * tick + mm[0]
    r = [flow, [players] + mm[1]]
    return r


dead_nodes = 0
for idx, n in enumerate(nodei):
    if n[0] == 0:
        dead_nodes |= 1 << idx
print(search(((0, 0), (0, 0)), 26, dead_nodes))
