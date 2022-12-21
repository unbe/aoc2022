from functools import cache
import operator

defs = {}

def mktask(task, name):
    if name == 'humn':
        return lambda: (1, 0)
    if ' ' in task:
        left, op, right = task.split(' ')

        @cache
        def ex():
            lmul, lc = defs[left]()
            rmul, rc = defs[right]()
            if name == 'root':
                return((rc - lc) / (lmul - rmul))
            if op == '/':
                if rmul != 0:
                    raise Exception("Non-linear: " + task)
                return (lmul/rc, lc/rc)
            if op == '*':
                if lmul != 0 and rmul != 0:
                    raise Exception("Non-linear: " + task)
                return (lmul * rc + rmul * lc, lc * rc)
            if op == '+':
                return (lmul + rmul, lc + rc)
            if op == '-':
                return (lmul - rmul, lc - rc)

        return ex
    else:
        return lambda: [0, int(task)]

with open("input.txt", "r") as f:
    for idx, line in enumerate(f):
        name, task = line.strip().split(':')
        defs[name] = mktask(task.strip(), name)

print(defs["root"]())
