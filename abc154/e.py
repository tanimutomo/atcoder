n = int(input())
k = int(input())

sm = 0
if n > 10**k:
  sm += n // 10**k
  sm += 10**k - 10**(k-1) - 10*(k-1)
else:
  sm += n - 10**(k-1) + 1
  sm -= n // 10**(k-1)
print(sm)