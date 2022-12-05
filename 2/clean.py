# print((lambda inp: [sum(win(p, r) for p, r in zip(map(lambda s: ord(s) - 64, inp[::2]), map(lambda s: ord(s) - 87, inp[1::2]))) for win in ((lambda p, r: (((r-2) % 3 + 1) == p)*6 + (r == p)*3 + r),(lambda p, r: ((r == 1) * (((p + 1) % 3) + 1)) or ((r == 2) * (p + 3)) or ((r == 3) * ((p % 3 + 1) + 6))))])(open("input.txt", "r").read().split()))

# (lambda inp: [
#     sum(win(p, r) for p, r in zip(
#         map(lambda s: ord(s) - 64, inp[::2]), map(lambda s: ord(s) - 87, inp[1::2])
#     )
# ) for win in ((lambda p, r: (((r-2) % 3 + 1) == p)*6 + (r == p)*3 + r),(lambda p, r: ((r == 1) * (((p + 1) % 3) + 1)) or ((r == 2) * (p + 3)) or ((r == 3) * ((p % 3 + 1) + 6))))])(open("input.txt", "r").read().split())
(lambda d:sum(((((((r-2)%3+1)==p)*6+(r==p)*3+r)+1j*(((r==1)*(((p+1)%3)+1))or((r==2)*(p+3))or((r==3)*((p%3+7)))))for p,r in map(lambda t:(ord(t[0])-64,ord(t[1])-87),zip(d[::2],d[1::2])))))(open("input.txt", "r").read().split())

