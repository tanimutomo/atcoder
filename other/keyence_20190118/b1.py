import numpy as np
n = int(input())
rs = [list(map(int, input().split())) for _ in range(n)]
rs = np.array(rs)
lr = np.stack([rs[:, 0] - rs[:, 1], rs[:, 0] + rs[:, 1]], axis=1)
lr = mn_mx[np.argsort(lr[:, 1])]

cnt = 0
reach = None
for l, r in lr:
    if reach is not None and l < reach:
        continue
    reach = r
    cnt += 1
print(cnt)