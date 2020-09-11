n, k = map(int, input().split())
ps = list(map(lambda n: (int(n)+1)/2, input().split()))

mx = sum(ps[:k])
sm = sum(ps[:k])
for i in range(k, n):
  sm += ps[i] - ps[i-k]
  if sm > mx:
    mx = sm
print(mx)