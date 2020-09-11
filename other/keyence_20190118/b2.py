n = int(input())
rs = [list(map(int, input().split())) for _ in range(n)]
lr = [[x-l, x+l] for x, l in rs]
lr.sort(key=lambda x: x[1])

cnt = 0
reach = None
for l, r in lr:
    if reach is not None and l < reach:
        continue
    reach = r
    cnt += 1
print(cnt)