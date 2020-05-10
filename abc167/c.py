n, m, x = map(int, input().split())
bs = [list(map(int, input().split())) for _ in range(n)]

from itertools import combinations

combs = list()
for k in range(1, n+1):
    combs.extend(list(combinations(range(0, n), k)))

mn = -1
for comb in combs:
    money = 0
    us = [0] * m
    for i in list(comb):
        b = bs[i]
        money += b[0]
        for j, u in enumerate(b[1:]):
            us[j] += u

    is_ok = True
    for i in range(m):
        if us[i] < x:
            is_ok = False
            break
    if is_ok:
        if mn < 0 or money < mn:
            mn = money

print(mn)