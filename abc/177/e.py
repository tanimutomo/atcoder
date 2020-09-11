n = int(input())
a = list(map(int, input().split()))


def gcd(x :int, y :int) -> int:
    if y == 0: return x
    return gcd(y, x%y)


def gcdn(l :list) -> int:
    if len(l) == 2: return gcd(*l)
    g = gcd(l[0], l[1])
    for li in l[2:]:
        g = gcd(g, li)
    return g

