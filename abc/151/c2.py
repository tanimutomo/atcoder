import numpy as np

n, m = [int(i) for i in input().split()]
ans = [input().split() for _ in range(m)]
ans = np.array(ans)

ps = ans[:, 0]
ss = ans[:, 1]
sub_ps = np.unique(ps)

cnt_c, cnt_w = 0, 0
for sp in sub_ps:
  indices = np.where(ps==sp)[0]
  s_sp = ss[indices]
  if np.all(s_sp == 'WA'):
    continue
  num_ws = np.where(s_sp == 'AC')[0][0]
  cnt_w += num_ws
  cnt_c += 1

print(cnt_c, cnt_w)