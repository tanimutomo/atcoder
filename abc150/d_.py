n, m = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
A = list(set(A))

ma = max(A)
bases = map(lambda x : x//2, A) 


i = 0
pre = 0
factor = 0
while True:
  v = ma // 2 + ma * i
  if v > m:
    break
  is_half = True
  for a, b in zip(A, bases):
    if (v - b) % a != 0:
      is_half = False
      break
  if is_half:
    print(v)
    if pre != 0:
      factor = v - pre
      break
    else:
      pre = v
  i += 1

print(i, pre, factor)
if factor == 0 and pre == 0:
  print(0)
elif factor == 0 and pre != 0:
  print(1)
else:
  print((m - ma//2) // factor)