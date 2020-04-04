n, k = map(int, input().split())
a = n%k
b = abs(a - k)
print(min(a, b))