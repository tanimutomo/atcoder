n = int(input())
a = list(map(int, input().split()))
a = list(map(lambda x: x - 1, a))

cnts = [0 for _ in range(n)]
for ai in a:
    cnts[ai] += 1

for cnt in cnts:
    print(cnt)