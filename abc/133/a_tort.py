n, a, b = [int(e) for e in input().split()]

tr = a * n
tx = b

if tr < tx:
    print(tr)
else:
    print(tx)
