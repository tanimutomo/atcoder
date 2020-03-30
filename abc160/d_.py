n, x, y = map(int, input().split())
x, y = x-1, y-1

am = list()
for i in range(n):
    if i == 0:
        ads = [i+1]
    elif i == n-1:
        ads = [i-1]
    else:
        ads = [i-1, i+1]
    if i == x:
        ads.append(y)
    elif i == y:
        ads.append(x)
    am.append(ads)

ans = [0 for _ in range(n)]
for i in range(n):
    queue = am[i]
    done = [False for _ in range(n)]
    d = 0
    while True:
        if len(queue) == 0: break
        now = queue.pop(0)
        if done[now]: continue
        ans[d] += 1
        done[now] = True
        queue.extend(am[now])

print(ans)