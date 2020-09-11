n, m = map(int, input().split())
ab_ = [list(map(int, input().split())) for _ in range(m)]

ab = []
for a, b in ab_:
    ab.append([a-1, b-1])

g_idx = [0] * n
g_sum = [0]
mrg = []

i = 1

for a, b in ab:
    if not g_idx[a] and not g_idx[b]:
        g_idx[a] = i
        g_idx[b] = i
        g_sum.append(2)
        i += 1
    elif g_idx[a] and not g_idx[b]:
        idx = g_idx[a]
        g_idx[b] = idx
        g_sum[idx] += 1
    elif g_idx[b] and not g_idx[a]:
        idx = g_idx[b]
        g_idx[b] = idx
        g_idx[a] = idx
        g_sum[idx] += 1
    else:
        mrg.append([g_idx[a], g_idx[b]])

g_inc = [[]] * (len(g_sum)+1)
mg_sum = g_sum
for g1, g2 in mrg:
    if g1 < g2:
        if g2 not in g_inc[g1]:
            g_inc[g1].append(g2)
            mg_sum[g1] += g_sum[g2]
    elif g2 < g1:
        if g1 not in g_inc[g2]:
            g_inc[g2].append(g1)
            mg_sum[g2] += g_sum[g1]

mx = 0
for s in g_sum + mg_sum:
    if s > mx:
        mx = s

print(mx)