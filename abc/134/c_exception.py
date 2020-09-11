n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

sa = sorted(a)
mx = sa[-1]
for val in a:
    if val != mx:
        print(sa[-1])
    else:
        print(sa[-2])
