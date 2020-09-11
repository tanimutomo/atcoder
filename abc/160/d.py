n, x, y = map(int, input().split())
x, y = x-1, y-1

am = list()
for i in range(n):
    if i == 0:
        ads = [i+1]
    else:
        ads = [i-1, i+1]
    if i == x:
        ads.append(y)
    elif i == y:
        ads.append(x)

for i in range(n):
    q = am[i]
    for j in len(q):
        if 