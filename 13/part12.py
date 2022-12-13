from input import a

def cast_values(l, r):
    if isinstance(l, int):
        l = [l]
    if isinstance(r, int):
        r = [r]
    return (l, r)

def comp(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l == r:
            return None
        return l < r
    elif isinstance(l, list) and isinstance(r, list):
        lw = False
        rw = False
        c = 0
        while True:
            try:
                li = l[c]
            except:
                lw = True

            try:
                ri = r[c]
            except:
                rw = True
            if lw and rw:
                return None
            if lw:
                return True
            if rw:
                return False

            e = comp(li, ri)
            if e is not None:
                return e
            c += 1
    else:
        l, r = cast_values(l, r)
        return comp(l, r)

print(list(map(lambda s: comp(*s), zip(a[::2], a[1::2]))))
s = 0
for idx, i in enumerate(list(map(lambda s: comp(*s), zip(a[::2], a[1::2]))), 1):
    if i:
        s+=idx

print(s) # part 1

from pprint import pprint
a.append([[2]])
a.append([[6]])
class IronMan:
    __slots__ = ("k")
    def __init__(self, k):
        self.k = k

    def __lt__(self, val):
        return comp(self.k, val.k)

    def __eq__(self, o):
        return self.k == o.k

    def __str__(self):
        return str(self.k)

    def __repr__(self):
        return str(self.k)

b = sorted(list(map(IronMan, a)))
# pprint(b)
print((b.index(IronMan([[2]])) +1) * (b.index(IronMan([[6]])) + 1)) # part 2