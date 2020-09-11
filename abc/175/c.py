x, k, d = map(int, input().split())

x_ = abs(x)

if x_ >= d * k:
    print(x_ - d*k)
    exit(0)

a = x_ % d
b = - (a - d)
k_ = x_ // d
l = k - k_

if l % 2 == 0:
    print(a)
else:
    print(b)