from decimal import *

# a, b = map(str, input().split())
# print((int(a) * int(float(b)*100)) // 100)

a, b = map(str, input().split())
print(Decimal(a) * Decimal(b) // 1)