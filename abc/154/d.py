n, k = map(int, input().split())
ps = list(map(lambda n: (int(n)+1)/2, input().split()))

mx = 0
for i in range(n - (k-1)):
  sm = sum(ps[i:i+k])
  if sm > mx:
    mx = sm
print(mx)