n, a, b = map(int, input().split())

ans = 0
ans += (n // (a+b)) * a
ans += min(n % (a+b), a)

print(ans)