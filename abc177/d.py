n, m = map(int, input().split())
ab_ = [list(map(int, input().split())) for _ in range(m)]

ab = []
for a, b in ab_:
    ab.append([a-1, b-1])

g_idx = [0] * n
g_sum = [0] * n
mrg = []

i = 1

def get_idx(i :int):
    for g_f, g_t in mrg:
        if g_f == i:
            i = g_t
    return i

for a, b in ab:
    if not g_idx[a] and not g_idx[b]:
        g_idx[a] = i
        g_idx[b] = i
        g_sum[i] += 2
        i += 1
    elif g_idx[a] and not g_idx[b]:
        idx = get_idx(g_idx[a])
        g_idx[b] = idx
        g_sum[idx] += 1
    elif g_idx[b] and not g_idx[a]:
        idx = get_idx(g_idx[b])
        g_idx[a] = idx
        g_sum[idx] += 1
    else:
        idx_a = get_idx(g_idx[a])
        idx_b = get_idx(g_idx[b])
        sum_a = g_sum[idx_a]
        sum_b = g_sum[idx_b]
        if sum_a >= sum_b:
            g_sum[idx_b] = 0
            g_sum[idx_a] += sum_b
            mrg.append([idx_b, idx_a])
        else:
            g_sum[idx_a] = 0
            g_sum[idx_b] += sum_a
            mrg.append([idx_a, idx_b])

mx = 0
for s in g_sum:
    if s > mx:
        mx = s

print(mx)