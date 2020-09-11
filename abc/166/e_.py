n = int(input())
a = list(map(int, input().split()))

# i < j
# j - i = Aj + Ai
# j - Aj = i + Ai

ans = 0
adds = dict()
for j in range(n):
    sub = j - a[j]
    if sub in adds.keys():
        ans += adds[sub]

    add = j + a[j]
    if add in adds.keys():
        adds[add] += 1
    else:
        adds[add] = 1

print(ans)
