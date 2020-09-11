n, k = map(int, input().split())
BASE = 10**9 + 7

def sm(mn :int, mx :int) -> int:
    n = mx - (mn - 1)
    return int((mx + mn) * (n / 2))

cnt = 0
for i in range(k, n+2):
    mn, mx = sm(0, i-1), sm(n-(i-1), n)
    cnt += mx - (mn-1)
    cnt = cnt % BASE
print(cnt)