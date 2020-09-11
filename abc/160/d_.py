n, x, y = map(int, input().split())
x, y = x-1, y-1


def update(dist, queue, d, x):
    if dist[x] >= 0: return dist, queue
    dist[x] = d+1
    queue.append(x)
    return dist, queue

ans = [0 for _ in range(n)]
for i in range(n):
    dist = [-1 for _ in range(n)]
    dist[i] = 0
    queue = [i]
    while True:
        if len(queue) == 0: break
        now = queue.pop(0)
        d = dist[now]
        if now-1 >= 0:
            dist, queue = update(dist, queue, d, now-1)
        if now+1 < n:
            dist, queue = update(dist, queue, d, now+1)
        if now == x:
            dist, queue = update(dist, queue, d, y)
        if now == y:
            dist, queue = update(dist, queue, d, x)
    for d in dist:
        ans[d] += 1

for a in ans[1:]:
    print(a//2)