n, k, s = map(int, input().split())

ans = [s for _ in range(k)]
if s == 10**9:
  ans += [1 for _ in range(n - k)]
else:
  ans += [s+1 for _ in range(n - k)]

print(*ans)