import re

pat = re.compile(r"Valve (.*) has flow rate=(.*); tunnels? leads? to valves? (.*)")

g = open("16/example.txt", "r").read().splitlines()

ret = "d = {"
for i in g:
    mat = pat.match(i)
    x = mat.groups()
    z = ", ".join(map(lambda s: "'" + s.strip() + "'", x[2].split(",")))
    ret += "'{0}': ({1}, [{2}]),\n".format(x[0], x[1], z)
ret += "}"

f = open("16/example.py", "w")
print(ret, file=f)
f.close()
