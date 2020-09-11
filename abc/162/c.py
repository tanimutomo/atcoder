import math

k = int(input())

def gcd(x, y):
    if y == 0: return x
    return gcd(y, x % y)

def gcd3(x, y, z):
    return gcd(gcd(x, y), z)

sm = 0
for i in range(1, k+1):
    for j in range(1, k+1):
        for l in range(1, k+1):
            sm += gcd3(i, j, l)
print(sm)