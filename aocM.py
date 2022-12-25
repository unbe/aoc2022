import re

world = []
with open("input.txt", "r") as f:
    while True:
        line = f.readline()
        if line == "\n":
            path = f.readline().strip()
            break

        world.append(line[:-1])
path=tuple((int(x[0]), x[1]) for x in re.findall(r'(\d+)(\D)?', path))
pos=[0, world[0].index('.'), 0]

dd = ((0, 1), (1, 0), (0, -1), (-1, 0))
dirs = "RDLU"
idir = "LURD"
N = len(world) // 4
print("N =", N)

"""
        CDDD
        C11E
        C11E
        C11E
AAAABBBB444F
N2223333444F
N2223333444F
MMMMLLLL444F
        K555GGGG
        K555666H
        K555666H
        JJJJIIIH
"""



def bigover(y, x, h):
    qy, qx = y // N, x // N
    py, px = y % N, x % N
    B = N - 1
    bpy, bpx = B - py, B - px
    if y == 2*N and qx == 0 and h == 3:   # case A -> B
        return (N + px, N, 0)
    if qy == 1 and x == N and h == 2: # case B -> A
        return (2*N, py, 1)

    if y == 2*N + B and qx == 1 and h == 1:   # case J -> K
        return (3*N + px, B, 2)
    if qy == 3 and x == B and h == 0:   # case K -> J
        return (2*N  + B, N + py, 3)

    if qy == 1 and x == N + B and h == 0:   # case G -> H
        return (B, 2*N + py, 3)
    if y == B and qx == 2 and h == 1:   # case H -> G
        return (N + px, N + B, 2)

    if qy == 0 and x == 2* N + B and h == 0:   # case F -> I
        return (2*N + bpy, N + B, 2)
    if qy == 2 and x == N + B and h == 0:   # case I -> F
        return (bpy, 2*N + B, 2)

    if y == 3*N + B and qx == 0 and h == 1:   # case L -> E
        return (0, 2*N + px, 1)
    if y == 0 and qx == 2 and h == 3:   # case E -> L
        return (3*N+B, px, 3)

    if qy == 2 and x == 0 and h == 2:   # case N -> C
        return (bpy, N, 0)
    if qy == 0 and x == N and h == 2:   # case C -> N
        return (2*N + bpy, 0, 0)

    if qy == 3 and x == 0 and h == 2:   # case M -> D
        return (0, N + py, 1)
    if y == 0 and qx == 1 and h == 3:   # case D -> M
        return (3*N + px, 0, 0)

    return None


def over(y, x, h):
    if N > 6:
        return bigover(y, x, h)

    qy, qx = y // N, x // N
    py, px = y % N, x % N
    B = N - 1
    bpy, bpx = B - py, B - px
    if y == N and qx == 0 and h == 3:   # case A -> D
        return (0, 2*N + bpx, 1)
    if y == 0 and qx == 2 and h == 3: # case D -> A
        return (N, bpx, 1)

    if y == N and qx == 1 and h == 3:   # case B -> C
        return (px, 2*N, 0)
    if qy == 0 and x == 2*N and h == 2: # case C -> B
        return (N, N + py, 1)
    
    if qy == 0 and x == 3*N-1 and h == 0: # case E -> H
        return (2*N + bpy, 4*N - 1, 2)
    if qy == 2 and x == 4*N-1 and h == 0: # case H -> E
        return (bpy, 3*N - 1, 2)
    
    if qy == 1 and x == 3*N-1 and h == 0: # case F -> G
        return (2*N, 3*N + bpy, 1)
    if y == N*2 and qx == 3 and h == 3: # case G -> F
        return (N + bpx, 3*N-1, 2)
    
    if qy == 1 and x == 0 and h == 2: # case N -> I
        return (3*N-1, 3*N + bpy, 3)
    if y == 3*N-1 and qx == 3 and h == 1: # case I -> N
        return (2*N - 1 - px, 0, 0)

    if y == 3*N-1 and qx == 2 and h == 1: # case J -> M
        return (2*N - 1, N - 1 - px , 3)
    if y == 2*N-1 and qx == 0 and h == 1: # case M -> J
        return (3*N-1, 2*N + bpx , 3)

    if qy == 2 and x == 2*N and h == 2: # case K -> L
        return (2*N - 1, N + bpy , 3)
    if y == 2*N-1 and qx == 1 and h == 1: # case L -> K
        return (2*N + bpx, 2*N, 0)

    return None


for y in range(N*4):
    for x in range(N*4):
        for h in range(4):
            o = over(y, x, h)
            if o is None:
                continue
            oy, ox, oh = o
            oh = idir.index(dirs[oh])
            oo = over(oy, ox, oh)
            if oo is None or oo[0] != y or oo[1] != x or oo[2] != idir.index(dirs[h]):
                print((y, x, h), '->', o, '->', (oy, ox, oh), '->', oo)
print("Self test done")

moves = 0
for _, i in enumerate(path):
    move, turn = i
    for nn in range(move):
        d = dd[pos[2]]
        ny, nx, nd = pos[0] + d[0], pos[1] + d[1], pos[2]
        oo = over(*pos)
        if oo is not None:
            ny, nx, nd = oo
        if world[ny][nx] != '.':
            if world[ny][nx] != '#':
                raise Exception("WUT??", ny, nx, world[ny][nx])
            break
        pos = [ny, nx, nd]
    if turn != '':
        drot = -1 if turn == "L" else 1
        pos[2] = (pos[2] + drot) % 4

print((pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + pos[2])
