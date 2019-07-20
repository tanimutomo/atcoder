n = int(input())
A = [int(i) for i in input().split()]
A.insert(0, 0)

boxes = dict()
have_balls = list()
for bn in range(n, 0, -1):
    a = A[bn]
    s = 0
    for t in range(2, n+1):
        if bn * t > n:
            break
        s += boxes[bn*t]

    if s % 2 == a:
        boxes[bn] = 0
    else:
        boxes[bn] = 1
        have_balls.append(str(bn))

print(len(have_balls))
print(' '.join(have_balls))
