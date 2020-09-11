from collections import deque

def breath_first_search(start :int, am :list):
    backs = [-1 for _ in range(n)]
    q = deque([start])
    visited = set([start])

    while True:
        if not q: break
        now = q.popleft()
        for node, is_adj in enumerate(am[now]):
            if not is_adj: continue
            if node in visited: continue
            backs[node] = now
            q.append(node)
            visited.add(node)

    return backs

n, m = map(int, input().split())
paths = [list(map(int, input().split())) for _ in range(m)]
am = [[0]*n for _ in range(n)]
for a, b in paths:
    am[a-1][b-1] = 1
    am[b-1][a-1] = 1

backs = breath_first_search(0, am)

if -1 in backs:
    print("Yes")

for back in backs[1:]:
    print(back+1)