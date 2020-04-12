n = int(input())
s = input()

INF = 1_000_000_000
colors = ['R', 'G', 'B']

def get_rest(si, sj):
    for c in colors:
        if not c in [si, sj]: return c

cnt = 0
for i in range(n):
    comb = 1
    for i, c in enumerate(colors):
        if c == s[i]: continue
        comb *= s[i+1:].count(c)
    cnt += comb

    w = 1
    while True:
        if i + 2*w >= n: break
        if s[i] != s[i+w] and s[i+w] != s[i+2*w] and s[i+2*w] != s[i]:
            cnt -= 1
        w += 1
print(cnt)