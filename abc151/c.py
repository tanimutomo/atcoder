n, m = [int(i) for i in input().split()]

cs = list()
cnt_c, cnt_w = 0, 0
for i in range(m):
  p, s = input().split()
  if p in cs:
    continue
  if s == 'AC':
    cnt_c += 1
    cs.append(p)
  else:
    cnt_w += 1

print(cnt_c, cnt_w)