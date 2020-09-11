n, m = map(int, input().split())
h = list(map(int, input().split()))
ab = [list(map(lambda x: int(x)-1, input().split())) for _ in range(m)]

is_good = [True] * n
for a, b in ab:
    if h[a] > h[b]:
        is_good[b] = False
    elif h[a] < h[b]:
        is_good[a] = False
    else:
        is_good[a] = False
        is_good[b] = False
print(sum(is_good))