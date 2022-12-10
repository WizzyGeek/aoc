g = open("10/input.txt", "r").read().split("\n")


tick = 0
c = 0
x = 1

states = {}

while tick < 241:
    try:
        i = g[c]
    except:
        break
    if i == "noop":
        tick += 1
        states[tick] = x
        c+=1
    else:
        _, k = i.split()
        states[tick + 1] = x
        states[tick + 2] = x
        tick += 2
        c+=1
        x+=int(k)

# import pprint
# pprint.pprint(states)

d=0
for i in range(20, 221, 40):
    d += states[i] * i

# print(d)

crt = ["  "] * 240
for i in range(len(crt)):
    x = states[i + 1]
    pixel_d = set([x +1, x, x-1])
    # print(pixel_d, i)
    if (i % 40) in pixel_d:
        crt[i] = "@@"

# print(crt, states)
for i in range(41, 242, 40):
    print("".join(crt[i-41:i]))
