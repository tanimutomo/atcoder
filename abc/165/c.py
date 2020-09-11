n, m, q = map(int, input().split())
ps_ = [list(map(int, input().split())) for _ in range(q)]

ps_ = sorted(ps_, key=lambda x: x[3], reverse=True)
ps = list()
for p in ps_:
    ps.append([p[0]-1, p[1]-1, p[2], p[3]])

score = 0
s = [0] * n
for p in ps:
    a, b, c, d = p
    if s[a] == 0 and s[b] == 0:
        s[a] = 1 if a == 0 else max(min(s[:a]), 1)
        if s[a] + c > m: continue
        s[b] = s[a] + c
        score += d
    elif s[a] == 0:
        if s[b] - c < 1: continue
        s[a] = s[b] - c
        score += d
    elif s[b] == 0:
        if s[a] + c > m: continue
        s[b] = s[a] + c
        score += d
    elif s[b] == s[a] + c:
        score += d
print(score)