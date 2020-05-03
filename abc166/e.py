n = int(input())
a = list(map(int, input().split()))

cnt = 0
dist = [a[0]-1] + a[1:]
for i, ai in enumerate(a[1:]):
    cnt += dist[:i+1].count(-ai)
    dist[:i+2] = list(map(lambda x: x-1, dist[:i+2]))

print(cnt)
