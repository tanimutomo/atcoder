import sys

a, b, c, k = map(int, input().split())
l = k
sm = 0

if a < l:
    sm += a
    l -= a
else:
    sm += l
    print(sm)
    sys.exit()

if b < l:
    l -= b
else:
    print(sm)
    sys.exit()

sm -=  l
print(sm)