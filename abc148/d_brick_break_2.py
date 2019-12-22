n = int(input())
A = [int(a) for a in input().split()]

is_over = False
now = 0

for a in A:
    if a == now+1:
        now += 1

if now == 0:
    print(-1)
else:
    print(n - now)