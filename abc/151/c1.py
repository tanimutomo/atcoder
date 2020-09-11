import numpy as np

n, m = [int(i) for i in input().split()]
to_i = dict(AC=1, WA=0)
ps = list()
ss = list()
for i in range(m):
  p, s = input().split()
  ps.append(int(p))
  ss.append(to_i[s])
ps = np.array(ps)
ss = np.array(ss)

sub_ps = np.unique(ps)

cnt_c, cnt_w = 0, 0
for sp in sub_ps:
  indices = np.where(ps==sp)[0]
  s_sp = ss[indices]
  if s_sp.sum() == 0:
    continue
  num_ws = np.where(s_sp == 1)[0][0]
  cnt_w += num_ws
  cnt_c += 1

print(cnt_c, cnt_w)