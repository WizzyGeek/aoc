g = open("11/input.txt", "r").read().split("\n\n")
import re

print(repr(g))

ret = "monkey = {"

j = []
for i in g:
    # i = i.split("\n")
    m = re.match(r"Monkey (\d): *\n *Starting items: (.*) *\n *Operation: new = (.*) *\n *Test: divisible by (\d+) *\n *If true: throw to monkey (\d+) *\n *If false: throw to monkey (\d+)", i)
    d = """{0}: {{
        "s": [{1}],
        "worry": lambda old: ({2}),
        "test": lambda w: w % {3},
        "c": ({4}, {5})
    }},
    """
    j.append(int(m.groups()[3]))
    ret += d.format(*m.groups()) # type: ignore

ret += "}"
# print(ret, file=open("11/part2/parsed.py", "w"))
from math import lcm
print(lcm(*j), j)