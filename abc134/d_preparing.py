n = int(input())
A = [int(i) for i in input().split()]

balls = list()
# for i, a in enumerate(reversed(A)):
for bn in range(n, 0, -1):
    a = A[bn - 1]
    if 2*bn > n:
        if a == 1:
            balls.append(str(bn))
    else:
        a2 = A[2*bn - 1]
        if a != a2:
            balls.append(str(bn))

all_balls = len(balls)
if all_balls % 2 != A[0]:
    print(-1)
else:
    print(all_balls)
    print(' '.join(balls))
