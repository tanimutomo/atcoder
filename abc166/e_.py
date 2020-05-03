n = int(input())
a = list(map(int, input().split()))

add = dict()
sub = dict()
for i, ai in enumerate(a):
    if i+ai in add.keys():
        add[i+ai] += 1
    else:
        add[i+ai] = 1
    if i-ai in sub.keys():
        add[i-ai] += 1
    else:
        add[i-ai] = 1

cnt = 0
for ak, av in add.items():
    if ak not in sub.keys(): continue
    cnt += av*sub[ak]

print(cnt)
