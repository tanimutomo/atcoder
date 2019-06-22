N, K = [int(e) for e in input().split()]
A = [int(a) for a in input().split()]

count = 0
sumA = sum(A)

r = 0
s = 0
ans = 0
for l in range(N):
    while s < K:
        if r == N:
            break
        s += A[r]
        r += 1
    if s < K:
        break
    ans += N - r + 1
    s -= A[l]

print(ans)
