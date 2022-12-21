from functools import cache
import operator

defs = {}
ops = {
        '/': operator.truediv,
        '*': operator.mul,
        '+': operator.add,
        '-': operator.sub
      }

def mktask(task):
    if ' ' in task:
        left, op, right = task.split(' ')

        @cache
        def ex():
            return ops[op](defs[left](), defs[right]())

        return ex
    else:
        return lambda: int(task)

with open("input.txt", "r") as f:
    for idx, line in enumerate(f):
        name, task = line.strip().split(':')
        defs[name] = mktask(task.strip())

print(defs["root"]())
