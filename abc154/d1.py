n, k = map(int, input().split())
ps = list(map(lambda n: (int(n)+1)/2, input().split()))

mx = sum(ps[:k])
for i in range(1, n - (k-1)):
  if ps[i-1] < ps[i+k-1]:
    mx = sum(ps[i:i+k])
print(mx)