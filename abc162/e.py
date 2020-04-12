from itertools import combinations

def gcd(x, y):
    if y == 0: return x
    return gcd(y, x % y)

def gcdn(l :list):
    if len(l) == 2: return gcd(*l)
    g = gcd(l[0], l[1])
    for li in l[2:]:
        g = gcd(g, li)
    return g

# n, k = map(int, input().split())
n, k = map(int, input().split())
k = k + 1

comb = list(combinations(range(1, k+1), n))

cnt = 0
for l in comb:
    unq = len(list(set(l)))
    cnt += (gcdn(l) * k**(unq - 1)) % (10**9 + 7)
print(cnt)