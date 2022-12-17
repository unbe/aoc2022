import re
nodes = {}
with open("input.txt", "r") as f:
    for _, line in enumerate(f):
        (valve, flow, exits) = re.match(r'Valve (..) has flow rate=(\d+); tunnels? leads? to valves? ((?:..(?:, |$))+)$', line).groups()
        exits = exits.split(', ')
        nodes[valve] = [int(flow), exits, None]

nodelist = sorted(nodes.keys())
W = dict([(x, {}) for x in nodelist])
for a in nodelist:
    for b in nodelist:
        W[a][b] = 1 if b in nodes[a][1] else 10**8

for k in nodelist:
  for i in nodelist:
    for j in nodelist:
      W[i][j] = min(W[i][j], W[i][k]+W[k][j])

import functools

@functools.cache
def search(nodename, tick, visited, d):
    node = nodes[nodename]
    tick -= 1
    flow = node[0] * tick
    mm = [0, []]
    visstep = visited.union(frozenset([nodename]))
    for step in set(nodelist) - visstep:
        if W[nodename][step] + 1 >= tick:
            continue
        if nodes[step][0] == 0:
            continue
        sflow, spath = search(step, tick - W[nodename][step], visstep, d+1)
        if sflow > mm[0]:
            mm = [sflow, spath]
    r = [flow + mm[0], [nodename] + mm[1]]
    return r

print(search('AA', 31, frozenset(), 0))
