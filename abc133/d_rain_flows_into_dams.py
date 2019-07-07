n = int(input())
A = [int(a) for a in input().split()]

x = 0
rains = [x]
for a in A:
    x = a - x
    rains.append(x)

diff = (rains[-1] - rains[0]) // 2
result = []
for i, x in enumerate(rains[:-1]):
    if i % 2 == 0:
        result.append(str((x + diff) * 2))
    else:
        result.append(str((x - diff) * 2))

print(' '.join(result))
