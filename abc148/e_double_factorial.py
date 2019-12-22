n = int(input())

def g(n, x):
    cnt = 0
    while True:
        n = n // x
        if x == 2:
            cnt += n
        else:
            cnt += n // 2
        if n == 0:
            break
    return cnt

if n % 2 != 0:
    print(0)
else:
    print(min(g(n, 2), g(n, 5)))