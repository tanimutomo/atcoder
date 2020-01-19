import numpy as np
n = int(input())
rs = [list(map(int, input().split())) for _ in range(n)]
rs = np.array(rs)
rs.sort(axis=0)

cnt = 0
reach = None
for i in range(n):
    x, l = rs[i]
    if i != 0 and x - l < reach:
        continue
    reach = x + l
    cnt += 1
print(cnt)