l, r = [int(i) for i in input().split()]

base = 2019
l_mod = l % base
r_mod = r % base

if r - l >= base:
    print(0)
elif r_mod <= l_mod:
    print(0)
else:
    print(l_mod * (l_mod + 1))
