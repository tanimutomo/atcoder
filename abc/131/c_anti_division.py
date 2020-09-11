a, b, c, d = [int(i) for i in input().split()]


def get_num(i):
    return b // i - (a-1) // i


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


all_num = b - a + 1
c_num = get_num(c)
d_num = get_num(d)
lcm = lcm(c, d)
lcm_num = get_num(lcm)

print(all_num - c_num - d_num + lcm_num)
