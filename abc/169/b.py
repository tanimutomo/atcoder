import sys

n = int(input())
a = list(map(int, input().split()))

l = 10**18

if 0 in a:
    print(0)
    sys.exit()

ans = 1
for ai in a:
    ans *= ai
    if ans > l:
        print(-1)
        sys.exit()

print(ans)