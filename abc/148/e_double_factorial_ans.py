n = int(input())

def g(n, x):
    f = 1 if x == 2 else 2
    if n == 0:
        return 0
    else:
        return g(n // x, x) + n // x // f

if n % 2 != 0:
    print(0)
else:
    print(min(g(n, 2), g(n, 5)))