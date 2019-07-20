n, d = [int(i) for i in input().split()]
cap = 2*d + 1
num = int(n / cap)
if n % cap != 0:
    num += 1
print(num)
