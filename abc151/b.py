n, k, m = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

s = sum(A)
o = m * n
if o - s > k:
  print(-1)
elif o - s < 0:
  print(0)
else:
  print(o - s)