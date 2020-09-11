n, k = map(int, input().split())
ps = list(map(int, input().split()))
cs = list(map(int, input().split()))

ps = [p-1 for p in ps]

visited = []
coarses = []
scores = []
while True:
    if len(visited) == n:
        break

    now = list(set(ps) - set(visited))[0]
    coarse = []
    score = []
    s, pre_s = 0, 0
    lp_cnt = 0
    visited_ = []

    while True:
        nxt = ps[now]
        if nxt in visited_:
            if lp_cnt != 0:
                break
            lp_cnt += 1
            visited_ = []

        s += cs[now]
        if cs[now] > 0:
            score.append(dict(bgn=pre_s, now=s, max=s))

        for sc in score:
            sc["now"] = s
            if sc["now"] > sc["max"]:
                sc["max"] = sc["now"]

        coarse.append(nxt)
        visited_.append(nxt)
        now = nxt
        pre_s = s
    
    scores += score
    coarses.append(coarse)
    visited += visited_

s_cands = []
for score in scores:
    s_cands.append(score["max"] - score["bgn"])

for coarse in coarses:
    sm = 0
    for i in coarse:
        sm += cs[i]
    s_cands.append(sm * (k // len(coarse)))

print(max(s_cands))