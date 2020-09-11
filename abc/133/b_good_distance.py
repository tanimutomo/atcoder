import math

n, d = [int(i) for i in input().split()]
xs = []
for i in range(n):
    xs.append([int(j) for j in input().split()])

count = 0
for i in range(n-1):
    for j in range(i+1, n):
        A = xs[i]
        B = xs[j]
        sum_ = 0
        for a, b in zip(A, B):
            sum_ += (a - b)**2
        decimal, integer = math.modf(math.sqrt(sum_))
        if decimal == 0:
            count += 1

print(count)
