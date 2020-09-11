def gcd(x :int, y :int) -> int:
    if y == 0: return x
    return gcd(y, x%y)


def gcdn(l :list) -> int:
    if len(l) == 2: return gcd(*l)
    g = gcd(l[0], l[1])
    for li in l[2:]:
        g = gcd(g, li)
    return g


def lcm(a :int, b :int) -> int:
    return a * b // gcd(a, b)


def main():
    print(gcd(12, 18))
    print(gcdn([12, 18, 54]))
    print(lcm(12, 18))


if __name__ == "__main__":
    main()