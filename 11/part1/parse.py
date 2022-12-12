g = open("11/example.txt", "r").read().split("\n\n")
import re

print(repr(g))

ret = "monkey = {"

for i in g:
    # i = i.split("\n")
    m = re.match(r"Monkey (\d): *\n *Starting items: (.*) *\n *Operation: new = (.*) *\n *Test: divisible by (\d+) *\n *If true: throw to monkey (\d+) *\n *If false: throw to monkey (\d+)", i)
    d = """{0}: {{
        "s": [{1}],
        "worry": lambda old: round(({2}) / 3),
        "test": lambda w: w % {3},
        "c": ({4}, {5})
    }},
    """
    ret += d.format(*m.groups()) # type: ignore

ret += "}"
print(ret, file=open("11/part1/parsed2.py", "w"))