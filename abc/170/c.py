import sys

x, n = map(int, input().split())
p = list(map(int, input().split()))

if not x in p:
    print(x)
    sys.exit()

i = 1
while True:
    if not x - i in p:
        print(x - i)
        sys.exit()
    if not x + i in p:
        print(x + i)
        sys.exit()
    i += 1