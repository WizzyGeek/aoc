(lambda p,d:(sum(p[(set(i[:l])&set(i[l:])).pop()]for i,l in map(lambda i:(i,len(i)>>1),d)),sum(p[(set(i)&set(j)&set(k)).pop()]for i,j,k in zip(d[::3],d[1::3],d[2::3]))))(dict(zip(__import__("string").ascii_letters,range(1, 53))),open("input.txt","r").read().split())

# version 3
# (
#     lambda p, d: (
#         sum(p[(set(i[:l]) & set(i[l:])).pop()] for i, l in map(lambda i: (i, len(i) // 2), d)),
#         sum(p[(set(i) & set(j) & set(k)).pop()] for i, j, k in zip(d[::3], d[1::3], d[2::3]))
#     )
# )(dict(zip(__import__("string").ascii_letters, range(1, 53))), open("input.txt", "r").read().split())

# version 2
# [
#     (
#         sum(p[(set(i[:l]) & set(i[l:])).pop()] for i, l in map(lambda i: (i, len(i) // 2), d)),
#         sum(p[(set(i) & set(j) & set(k)).pop()] for i, j, k in zip(d[::3], d[1::3], d[2::3]))
#     ) for p, d in [(dict(zip(__import__("string").ascii_letters, range(1, 53))), open("input.txt", "r").read().split())]
# ]

# [(sum(p[(set(i[:l])&set(i[l:])).pop()]for i,l in map(lambda i:(i,len(i)>>1),d)),sum(p[(set(i)&set(j)&set(k)).pop()]for i,j,k in zip(d[::3],d[1::3],d[2::3]))) for p,d in [(dict(zip(__import__("string").ascii_letters,range(1,53))),open("input.txt", "r").read().split())]]

# Version 1 from repl
# (
#     lambda p, d: [
#         h(p, d) for h in (
#             (
#                 (lambda h:
#                     (
#                         lambda p, d: sum(
#                             p[h(i, len(i) // 2).pop()] for i in d
#                         )
#                     )
#                 )(lambda m, l: set(m[:l]) & set(m[l:])),
#                 (
#                     lambda h: (
#                         lambda p, d: sum(p[h(i, j , k).pop()] for i, j, k in zip(d[::3], d[1::3], d[2::3]))
#                     )
#                 )(
#                     lambda i, j, k: set(i) & set(j) & set(k)
#                 )
#             )
#         )
#     ]
# )({j: i+1 for i, j in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")}, open("input.txt", "r").read().split())
