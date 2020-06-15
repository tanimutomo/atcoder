n = int(input())
a = list(map(int, input().split()))

a = sorted(a)

dp  = [0] * (a[-1]+1)

for ai in a:
    if dp[ai]:
        dp[ai] += 1
        continue

    i = 1
    while True:
        if ai*i >= len(dp):
            break
        dp[ai*i] += 1
        i += 1

ans = 0
for ai in a:
    if dp[ai] == 1:
        ans += 1

print(ans)