n, m = map(int, input().split())
a = list(map(int, input().split()))

s = sum(a)
l = s * (1/(4*m))

cnt = 0
for ai in a:
    if ai >= l:
        cnt += 1
if cnt >= m:
    print('Yes')
else:
    print('No')