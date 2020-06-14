def cmin(l):
    mn = 10000000000000
    for li in l:
        if li < mn and li != 0:
            mn = li
    return mn

n, q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(q)]

smx = [0]*(2*10**5)
smen = [[]]*(2*10**5)
for i, (a, b) in enumerate(ab):
    if smx[b] < a:
        smx[b] = a
    smen[b].append(i)

mn = cmin(smx)

for c, d in cd:
    a, b = ab[c]
    if smx[b] != a:
        ab[c][1] = d
        smen[b].remove(c)
        print(mn)
        continue

    mx = 0
    for i in smen[b]:
        if mx < ab[i][0]:
            mx = ab[i][0]
    smx[b] = mx
    ab[c][1] = d
    smen[b].remove(c)

    mn = cmin(smx)
    print(mn)