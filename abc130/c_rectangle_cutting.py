W, H, x, y = [int(e) for e in input().split()]
if 2*x == W and 2*y == H:
    print(W*H / 2, 1)
else:
    print(W*H / 2, 0)
