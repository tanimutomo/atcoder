n, m = [int(i) for i in input().split()]
ans = [input().split() for _ in range(m)]

is_ac = [0 for i in range(n)]
cnt_wa = [0 for i in range(n)]
for p, s in ans:
  p = int(p) - 1
  if is_ac[p]:
    continue
  if s == 'AC':
    is_ac[p] = 1
  else:
    cnt_wa[p] += 1

cor = sum(is_ac)
pena = 0
for p, c in enumerate(is_ac):
  if c:
    pena += cnt_wa[p]

print(cor, pena)