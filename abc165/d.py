a, b, n = map(int, input().split())

if b == 1:
    x = 0
if n < b:
    x = n
else:
    x = b - 1
print((a*x)//b - a*(x//b))