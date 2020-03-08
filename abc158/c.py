import math

a, b = map(int, input().split())

na = [a / 0.08, (a+1) / 0.08]
nb = [b / 0.1,  (b+1) / 0.1 ]

def adjust_float(l):
    mn, mx = l
    return [
        math.ceil(mn),
        math.floor(mx) if mx % 1 != 0 else int(mx - 1),
    ]

na = adjust_float(na)
nb = adjust_float(nb)

if nb[1] < na[0] or na[1] < nb[0]:
    print(-1)
elif na[0] <= nb[0] and nb[0] <= na[1]:
    print(int(nb[0]))
elif nb[0] <= na[0] and na[0] <= nb[1]:
    print(int(na[0]))
